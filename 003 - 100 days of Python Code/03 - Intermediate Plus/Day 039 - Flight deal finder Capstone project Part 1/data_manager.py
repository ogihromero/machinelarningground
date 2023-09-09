import requests
from decouple import config

SHEETY_ENDPOINT = config("SHEETY_ENDPOINT")
SHEETY_HEADERS = {"Authorization": config("SHEETY_TOKEN")}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.data: dict[str, str] = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        self.data = response.json()["prices"]
        return self.data

    def update_data(self):
        for city in self.data:
            updated_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=updated_data,
                headers=SHEETY_HEADERS,
            )
            print(response.text)
