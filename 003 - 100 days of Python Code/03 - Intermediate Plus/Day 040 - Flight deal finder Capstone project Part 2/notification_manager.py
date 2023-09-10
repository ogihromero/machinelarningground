import smtplib
from decouple import config

EMAIL_PROVIDER_SMTP_ADDRESS = config("MY_EMAIL")
MY_EMAIL = config("SMTP")
MY_PASSWORD = config("PASSWORD")


class NotificationManager:
    # Class responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        pass

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode(
                        "utf-8"
                    ),
                )
