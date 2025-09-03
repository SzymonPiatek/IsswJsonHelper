import os
import requests
from typing import TypedDict


class LoginData(TypedDict):
    email: str
    password: str


class Postman:
    def __init__(self, base_url: str, login_data: LoginData):
        self.base_url = base_url
        self.login_data = login_data
        self.access_token = None

        self.login()

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
            print("Zalogowano poprawnie. Access token zapisany.")
        else:
            raise Exception(f"Logowanie nie powiodło się: {response.status_code}, {response.text}")

    def application_autosave(self, form_id: int, json: object):
        url = f"{self.base_url}/api/v1/applications/{form_id}/autosave"

        response = requests.put(
            url,
            json=json,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            },
            verify=False
        )

        if response.status_code == 200:
            print(f"Nadpisano wniosek: {form_id}")
        else:
            raise Exception(f"Operacja nie powiodła się ({form_id}): {response.status_code}, {response.text}")

    def application_pdf(self, output_path: str, json: object):
        url = f"{self.base_url}:5000/pdf/"
        output_file_path = f"{output_path}/file.pdf"
        os.makedirs(output_path, exist_ok=True)

        response = requests.post(
            url,
            json={
                "jrwa_file": "",
                "form": json
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            verify=False
        )

        if response.status_code == 200:
            with open(output_file_path, 'wb') as f:
                f.write(response.content)
            print(f"PDF zapisany do: {output_file_path}")
        else:
            raise Exception(f"Generowanie PDF nie powiodło się: {response.status_code}, {response.text}")
