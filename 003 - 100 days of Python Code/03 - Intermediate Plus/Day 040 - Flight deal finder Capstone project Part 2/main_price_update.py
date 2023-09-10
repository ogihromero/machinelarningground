from data_manager import DataManager
from flight_search import FlightSearch
from decouple import config
from datetime import datetime, timedelta
from telegram_bot import telegram_bot_sendtext
from notification_manager import NotificationManager


notification_manager = NotificationManager()
ORIGIN_CITY_IATA = config("ORIGIN_CITY_IATA")
data_manager = DataManager()
sheet_data = data_manager.get_flight_data()

flight_search = FlightSearch()

data_changed = False
for city in sheet_data:
    if city.get("iataCode") == "" or city.get("iataCode") is None:
        city["iataCode"] = flight_search.get_destination_code(city["city"])
        data_changed = True

if data_changed:
    data_manager.flight_data = sheet_data
    data_manager.update_flight_data()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_client_data()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = (
            f"Low price alert! Only £{flight.price} to fly from"
            f"{flight.origin_city}-{flight.origin_airport} to"
            f"{flight.destination_city}-{flight.destination_airport},"
            f" from {flight.out_date} to {flight.return_date}."
        )
        if flight.stop_overs > 0:
            message += (
                f"\nFlight has {flight.stop_overs} stop over,"
                f"via {flight.via_city}."
            )
        notification_manager.send_emails(emails, message)
        telegram_bot_sendtext(bot_message=message)
