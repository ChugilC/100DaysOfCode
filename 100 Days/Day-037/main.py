import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "chugil"
TOKEN = "100DaysOfPython"
GRAPHID = "graph1"
NAME = "Running Graph"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CREATE user account 
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": NAME,
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# CREATE graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

# POST value to the graph
graph_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

graph_value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.0"

}

# response = requests.post(url=graph_value_endpoint,json=graph_value_config ,headers=headers)
# print(response.text)

# UPDATE graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "8.0"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# DELETE pixela
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)