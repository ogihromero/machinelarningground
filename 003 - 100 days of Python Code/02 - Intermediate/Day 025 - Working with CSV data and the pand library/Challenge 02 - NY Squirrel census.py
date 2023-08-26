# Central Park Squirrel Data Analysis
import pandas
from os import path


def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


data = pandas.read_csv(
    dir("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
)

colours_data = data["Primary Fur Color"].value_counts()

print(f"Total Gret squirrels: {colours_data.loc['Gray']}")

colours_data.to_csv(dir("squirrel_count.csv"))
