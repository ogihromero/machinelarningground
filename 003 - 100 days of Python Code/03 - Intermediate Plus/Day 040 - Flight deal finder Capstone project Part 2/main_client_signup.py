from data_manager import DataManager


data_manager = DataManager()
# sheet_data = data_manager.get_client_data()

print(
    "Welcome to Ogih's Flight Club.\n \
We find the best flight deals and email them to you."
)

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = ""
email_confirmation = "confirmation"
while email1 != email_confirmation:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()
    email_confirmation = input("Please verify your email : ")
    if (
        email_confirmation.lower() == "quit"
        or email_confirmation.lower() == "exit"
    ):
        exit()

print("OK. You're in the club!")

data_manager.post_new_client(first_name, last_name, email1)
