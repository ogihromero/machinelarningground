import requests


CITY = "Brasília"
CITY_LAT = -15.826691
CITY_LONG = -47.921822
parameters = {"lat": CITY_LAT, "long": CITY_LONG}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters
)


data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(
    f"In {CITY}, the current sunrise is at {sunrise} and"
    + f" the sunset at {sunset}"
)
