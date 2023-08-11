# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """ Get the year and month and returns how many days it'll have, taking leap years into account."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    elif month > 12 or month < 1:
        return "Invalid month."
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month (1 to 12): "))
days = days_in_month(year, month)
print(days)
