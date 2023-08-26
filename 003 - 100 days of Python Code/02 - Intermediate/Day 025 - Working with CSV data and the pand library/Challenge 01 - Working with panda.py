from os import path
import pandas


# Function to get the directory of the path
# So files won't be read/written from the root directory (machinelarningground)
def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


# import csv
# with open(
#     path.join(path.dirname(__file__), "weather_data.csv"), "r"
# ) as weather_file:
#     # data = weather_file.read().splitlines()
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)


data = pandas.read_csv(dir("weather_data"))
# print(data)

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
print(f"Max temperature: {data['temp'].max()}")

# Data in columns
# print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(f"Maximum temperature in: {data[data.temp == data.temp.max()]}")

monday = data[data.day == "Monday"]
print(f"Monday's temperature in Fº = {(monday.temp[0] * 9/5 + 32)}")

# Create dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
data.to_csv(dir("new_data.csv"))
