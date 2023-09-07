from decouple import config
import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = config("USER_TOKEN")
USERNAME = config("USER")
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "watched-episodes"

headers = {"X-USER-TOKEN": config("USER_TOKEN")}
# # Creating User on https://pixe.la
# user_parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_parameters)


# # Creating a graph
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Watched Episodes",
#     "unit": "episode",
#     "type": "int",
#     "color": "shibafu",
#     "timezone": "America/Sao_Paulo",
# }

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers
# )

# Working with pixels
create_pixel_endpoint = f"{graph_endpoint}/watched-episodes"
today = datetime.now().strftime("%Y%m%d")
update_pixel_endpoint = f"{create_pixel_endpoint}/{today}"
pixel_config = {
    "date": today,
    "quantity": "41",
    "optionalData": '{"One Piece":"200-241"}',
}


# Posting a Pixel
response = requests.post(
    url=create_pixel_endpoint,
    json=pixel_config,
    headers=headers,
)


# # Updating a pixel
# response = requests.put(
#     url=update_pixel_endpoint, headers=headers, json=pixel_config
# )

# Deleting a pixel
# response = requests.delete(url=update_pixel_endpoint, headers=headers)

# Showing query result
print(response.text)
