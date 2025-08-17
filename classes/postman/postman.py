import requests


class Postman:
    def __init__(self, base_url: str, email: str, password: str):
        self.base_url = base_url
        self.email = email
        self.password = password
        self.access_token = None

    def login(self):
        login_url = f"{self.base_url}/token/"

        response = requests.post(
            login_url,
            json={
                "email": self.email,
                "password": self.password
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
        url = f"{self.base_url}/applications/{form_id}/autosave"

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
            raise Exception(f"Operacja nie powiodła się: {response.status_code}, {response.text}")
