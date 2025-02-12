import requests
import json

API_URL = "https://api.gethypercube.com/vendors?sortBy=createdAt:desc"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "Content-Type": "application/json"
}

response = requests.get(API_URL, headers=HEADERS)
data = response.json()

with open("/var/ossec/logs/hypercube_logs.json", "w") as file:
    json.dump(data, file)
