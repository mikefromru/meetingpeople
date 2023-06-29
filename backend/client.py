import requests

url = 'http://localhost:8000/api-token-auth/'

payload = {
        'username': 'admin',
        'password': 'admin',
    }

r = requests.post(url, data=payload)
print(r.json())
