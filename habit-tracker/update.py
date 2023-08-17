from main import PIXELA_ENDPOINT, USERNAME, GRAPH_ID, graph_headers
import datetime
import requests

today = datetime.datetime.now()
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data={
    "quantity": "4"
}

# Commented out because it was used to update a pixel on the graph.
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=graph_headers)
print(response.text)