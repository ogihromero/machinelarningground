import requests
from decouple import config

SHEETY_ENDPOINT = config("SHEETY_ENDPOINT")
SHEETY_HEADERS = {"Authorization": config("SHEETY_TOKEN")}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.flight_data: dict[str, str] = {}
        self.client_data: dict[str, str] = {}

    def get_flight_data(self):
        response = requests.get(
            url=f"{SHEETY_ENDPOINT}/prices", headers=SHEETY_HEADERS
        )
        self.flight_data = response.json()["prices"]
        return self.flight_data

    def update_flight_data(self):
        for city in self.flight_data:
            updated_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/prices/{city['id']}",
                json=updated_data,
                headers=SHEETY_HEADERS,
            )
            print(response.text)

    def get_client_data(self):
        response = requests.get(
            url=f"{SHEETY_ENDPOINT}/users", headers=SHEETY_HEADERS
        )
        self.client_data = response.json()["users"]
        return self.client_data

    def post_new_client(self, first_name, last_name, email):
        url = f"{SHEETY_ENDPOINT}/users/"

        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        response = requests.post(url=url, headers=SHEETY_HEADERS, json=body)
        response.raise_for_status()
        print(response.text)
