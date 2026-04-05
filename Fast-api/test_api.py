import requests
from pprint import pprint

url = "http://127.0.0.1:8000/process-data"

data = {
    "numbers": [1, 2, 3, -5, 100],
    "threshold": 10
}

response = requests.post(url, json=data)

# print("Input:", data)
# print("Output:", response.json())

print("Input:")
pprint(data)

print("\nOutput:")
pprint(response.json())