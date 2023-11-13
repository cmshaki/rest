import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "proverbs11:25", "price": 33.00}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
