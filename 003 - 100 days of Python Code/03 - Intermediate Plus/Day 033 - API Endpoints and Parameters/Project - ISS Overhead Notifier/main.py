import requests
from datetime import datetime
import smtplib
from decouple import config
from os import path
import time


def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


MY_LAT = -15.826691  # Your latitude
MY_LONG = -47.921822  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True

    # Your position is within +5 or -5 degrees of the ISS position.


def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters
    )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_nighttime():
        my_email = config("DAY_33_EMAIL")
        my_password = config("DAY_33_PASSWORD")
        with smtplib.SMTP(config("DAY_33_SMTP")) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:Look UP!\n\nThe ISS is overhead",
            )
