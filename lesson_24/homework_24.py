import requests
from requests.auth import HTTPBasicAuth

# POST /auth
auth_url = "http://127.0.0.1:8080/auth"
auth = HTTPBasicAuth("test_user", "test_pass")
response = requests.post(auth_url, auth=auth)

print(response.json())

access_token = response.json()['access_token']

# GEt /cars
cars_url = "http://127.0.0.1:8080/cars"
headers = {"Authorization": f"Bearer {access_token}"}
params = {"sort_by": "price", "limit": 5}
response = requests.get(cars_url, headers=headers, params=params)

print(response.json())