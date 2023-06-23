import requests
import json

url = "https://api.easybroker.com/v1/contact_requests?page=1&limit=20"

headers = {
    "accept": "application/json",
    "X-Authorization": "v486r4zj9eg7jrte19pu95jkatly9d"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    formatted_response = json.dumps(data, indent=2)
    print(formatted_response)
else:
    print("Error en la solicitud:", response.text)