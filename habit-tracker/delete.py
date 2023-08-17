from main import PIXELA_ENDPOINT, USERNAME, GRAPH_ID, graph_headers
import datetime
import requests

delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20230727"

# Commented out because it was used to delete a pixel on the graph.
response = requests.delete(url=delete_endpoint, headers=graph_headers)
print(response.text)