import requests
from .models.invoice import Invoice


class LexOfficeClient:
    def __init__(self, api_key) -> None:
        self.base_url = "https://api.lexoffice.io/v1"
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def ping(self) -> bool:
        response = requests.get(f"{self.base_url}/ping", headers=self.headers)

        if response.status_code == 200:
            print("Connected to Lexoffice Public API successfully")
            print(f"User:{response.json()['userEmail']} ")

            return True
        else:
            print("Connection to Lexoffice Public API failed.")
            print(f"Error: {response.json()}")
            return False

    def create_invoice(self, invoice: Invoice) -> bool:
        response = requests.post(
            f"{self.base_url}/invoices",
            headers=self.headers,
            data=invoice,
        )

        if response.status_code == 201:
            print("Invoice created successfully")
            print(f"ID: {response.json()['id']}")
            return True
        else:
            print("Invoice creation failed.")
            print(f"Error: {response.json()}")
            return False
