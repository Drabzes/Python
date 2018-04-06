from const import get_token
import json
import requests

api_token = "RGAPI-f09320a2-a0a7-403c-82bf-0395ca1e1f30"
headers = {'Content-Type': 'application/json'}

def get_summoner_by_name(name):
    api_url = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + name + get_token()

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
