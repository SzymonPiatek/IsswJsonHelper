import os
import requests
from typing import TypedDict, Literal
import urllib3
from urllib3.exceptions import InsecureRequestWarning


urllib3.disable_warnings(InsecureRequestWarning)


class LoginData(TypedDict):
    email: str
    password: str


class Postman:
    def __init__(self, base_url: str, login_data: LoginData):
        self.base_url = base_url
        self.login_data = login_data
        self.access_token = None

    def construct_form_link(self, json_type: Literal["application", "report"], form_id: int):
        return f"{self.base_url}/{'wniosek' if json_type == 'application' else 'raport'}/{form_id}/edycja?version=-1"

    def login(self):
        login_url = f"{self.base_url}/api/v1/token/"

        response = requests.post(
            login_url,
            json={
                "email": self.login_data["email"],
                "password": self.login_data["password"],
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            verify=False
        )

        if response.status_code == 200:
            self.access_token = response.json().get("access")
            print(f"Zalogowano na {self.base_url}.\nAccess token zapisany.")
        else:
            raise Exception(f"Logowanie na {self.base_url} się powiodło nie:\n- status: {response.status_code},\n- text: {response.text}")

    def form_autosave(self, form_id: int, json: object):
        url = f"{self.base_url}/api/v1/{'reports' if json.json_type == 'report' else 'applications'}/{form_id}/autosave"

        response = requests.put(
            url,
            json=json.output_json,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            },
            verify=False
        )

        form_url = self.construct_form_link(json_type=json.json_type, form_id=form_id)

        if response.status_code == 200:
            print(f"Nadpisano schemę {'raportu' if json.json_type == 'report' else 'wniosku'}: {form_url}")
        else:
            raise Exception(f"Operacja nie powiodła: ({form_url}) - {response.status_code}, {response.text}")

    def form_update_schema(self, form_id: int, json: object):
        url = f"{self.base_url}/api/v1/cms/{'reports' if json.json_type == 'report' else 'applications'}/{form_id}/schema"

        response = requests.patch(
            url,
            json=json.output_json,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            },
            verify=False
        )

        form_url = self.construct_form_link(json_type=json.json_type, form_id=form_id)

        if response.status_code == 200:
            message = response.json().get("message", "")

            if message == f"Zaktualizowano scheme dla {'raportu' if json.json_type == 'report' else 'aplikacji'}.":
                print(f"Zaktualizowano schemę {'raportu' if json.json_type == 'report' else 'wniosku'}: {form_url}")
                return True
            else:
                return False
        else:
            # raise Exception(f"Operacja nie powiodła się ({self.base_url, form_id}): {response.status_code}, {response.text}")
            return False

    def form_pdf(self, output_path: str, output_file: str, json_type: Literal["application", "report"], form_id: int):
        url = f"{self.base_url}/api/v1/{json_type}s/{form_id}/working_pdf"
        os.makedirs(output_path, exist_ok=True)
        output_file_path = (
            output_path / output_file
        )

        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {self.access_token}",
                "Accept": "*/*",
            },
            verify=False,
            stream=True
        )

        if response.status_code == 200:
            with open(output_file_path, 'wb') as f:
                f.write(response.content)
            print(f"PDF zapisany do: {output_file_path}")
        else:
            raise Exception(f"Generowanie PDF nie powiodło się ({self.base_url, form_id}: {response.status_code}, {response.text}")
