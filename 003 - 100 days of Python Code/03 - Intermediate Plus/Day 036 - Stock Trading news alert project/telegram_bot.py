from decouple import config
import requests


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
    response.raise_for_status()
    return response.json()
