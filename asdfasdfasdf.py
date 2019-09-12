import requests

headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': 'zc4jzl9wci2c16d2zir99z0jz7lxpw',
    'Authorization': 'OAuth m9aomgcvgacww3ybeo07m2pu162c0y',
}

params = (
    ('login', 'thiseguy'),
)

response = requests.get('https://api.twitch.tv/kraken/users', headers=headers, params=params)
print(response.text)
