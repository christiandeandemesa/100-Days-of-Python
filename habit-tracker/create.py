from main import PIXELA_ENDPOINT, USERNAME, GRAPH_ID, graph_headers
import datetime
import requests

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now()
pixel_data = {
    # Formats the today's date into YYYYMMDD.
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=graph_headers)
print(response.text)