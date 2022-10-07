import requests

r = requests.post(
    'https://api.mishasaidov.com/login',
    json={
        'login': 'ilya@vtb.ru',
        'password': 'Cvb852456',
    },
)
print(r.text)
