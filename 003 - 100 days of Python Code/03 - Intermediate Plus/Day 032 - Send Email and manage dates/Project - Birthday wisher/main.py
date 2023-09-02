import smtplib
from decouple import config
from datetime import datetime as dt
from os import path
import pandas
import random


def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


my_email = config("DAY_32_EMAIL")
my_password = config("DAY_32_PASSWORD")


today_tuple = (dt.now().month, dt.now().day)
data = pandas.read_csv(dir("birthdays.csv"))
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    name = birthdays_dict[today_tuple]["name"]
    email = birthdays_dict[today_tuple]["email"]
    with open(
        dir(f"letter_templates/letter_{random.randint(1,3)}.txt"), "r"
    ) as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)
    with smtplib.SMTP(config("DAY_32_SMTP")) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday {name}!!!!\n\n{letter}",
        )
