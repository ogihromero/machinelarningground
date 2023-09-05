import requests
from decouple import config
import schedule
import time

parameters = {
    "appid": config("API_KEY"),
    "lat": -19.917299,
    "lon": -43.934559,
    "exclude": "current,minutely,daily",
}


response = requests.get(
    "https://api.openweathermap.org/data/2.8/onecall", params=parameters
)
response.raise_for_status()
weather_data = response.json()


def telegram_bot_sendtext(bot_message):
    bot_token = config("BOT_TOKEN")
    bot_chatID = config("CHAT_ID")
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + bot_chatID
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)

    return response.json()


def report():
    will_rain = False
    weather_slice = weather_data["hourly"][:12]
    for hour in weather_slice:
        if hour["weather"][0]["id"] < 700:
            will_rain = True
    if will_rain:
        telegram_bot_sendtext("Bring an umbrella, it will rain ☂️")


schedule.every().day.at("07:00").do(report)


while True:
    schedule.run_pending()
    time.sleep(1)
