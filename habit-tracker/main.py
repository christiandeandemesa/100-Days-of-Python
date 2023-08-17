import requests

USERNAME="dyslecix"
TOKEN="test1234"
GRAPH_ID="graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Commented out because it was used to create a pixela account.
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ichou"
}
graph_headers = {
    "X-USER-TOKEN": TOKEN
}

# Commented out because it was used to create a graph.
# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(response.text)