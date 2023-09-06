from decouple import config
from telegram_bot import telegram_bot_sendtext
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": config("STOCK_API_KEY"),
}

news_parameters = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "apiKey": config("NEWS_API_KEY"),
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

before_yesterday_data = data_list[1]
before_yesterday_closing_price = float(before_yesterday_data["4. close"])

difference = yesterday_closing_price - before_yesterday_closing_price
percentange_diff = (difference / yesterday_closing_price) * 100
up_down = "🔺" if difference > 0 else "     🔻"

if abs(percentange_diff) > 4:
    news_response = requests.get(NEWS_ENDPOINT, news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{percentange_diff:.2f}% \n"
        f"Headline: {article['title']}. \nBrief: {article['description']}"
        for article in articles
    ]
    for article in formatted_articles:
        telegram_bot_sendtext(article)
