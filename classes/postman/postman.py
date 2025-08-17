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
