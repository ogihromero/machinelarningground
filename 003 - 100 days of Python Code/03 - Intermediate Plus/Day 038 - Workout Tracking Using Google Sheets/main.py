import requests
from decouple import config
from datetime import datetime


NUTRI_APP_ID = config("NUTRITIONIX_APP_ID")
NUTRIX_API_KEY = config("NUTRITIONIX_API_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = config("SHEETY_ENDPOINT")


user_input = input("Tell me what exercises you did: ")
nutrix_headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRIX_API_KEY,
}
nutrix_parameters = {
    "query": user_input,
    "gender": config("ENV_GENDER"),
    "weight_kg": config("ENV_WEIGHT"),
    "height_cm": config("ENV_HEIGHT"),
    "age": config("ENV_AGE"),
}
response = requests.post(
    url=exercise_endpoint, headers=nutrix_headers, json=nutrix_parameters
)
response.raise_for_status()
result = response.json()

sheety_headers = {"Authorization": config("SHEETY_TOKEN")}

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        sheety_endpoint, json=sheety_parameters, headers=sheety_headers
    )

    print(sheet_response.text)
