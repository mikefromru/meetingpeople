import requests

url = 'http://localhost:8000/api/clients/like/'

r = requests.post(url, data={'user_1': 'liked_user_2'})
print(r.json())

