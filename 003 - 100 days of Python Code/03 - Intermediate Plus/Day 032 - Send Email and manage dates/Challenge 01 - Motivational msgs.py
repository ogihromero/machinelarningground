import smtplib
from decouple import config
import datetime as dt
from os import path
import random


def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


my_email = config("DAY_32_EMAIL")
my_password = config("DAY_32_PASSWORD")

# weekday in integer
weekday = dt.datetime.now().weekday()

# weeday in string format
# weekday = dt.datetime.now().strftime("%A")
if weekday == 1:
    with open(dir("quotes.txt"), "r") as file:
        quotes = file.read().splitlines()
        quote = random.choice(quotes)
    with smtplib.SMTP(config("DAY_32_SMTP")) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            # msg="Subject:A quote for this {weekday}\n\n{quote}l",
            msg=f"Subject:Monday Motivation\n\n{quote}l",
        )
# connection.close()
