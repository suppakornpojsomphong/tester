import requests
from pprint import pprint


url = "http://127.0.0.1:5000/process-data"

data = {
    "numbers": [1, 2, 3, -5, 100],
    "threshold": -1
}

response = requests.post(url, json=data)

print("\nOutput:")
pprint(response.json())