import time

from const import get_token
import json
import requests

api_token = "?api_key=RGAPI-83251416-6798-4b1d-8538-457d1872af06"
headers = {'Content-Type': 'application/json'}


def get_matches_from_accountId(accountId):
    api_url = "https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + accountId + get_token()

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        time.sleep(1)
        print("sleeping for 1 second inside get_matches_from_accountId")
        get_matches_from_accountId(accountId)
    else:
        print(response.status_code)
        return response.status_code


def get_match_from_account(matchId):
    api_url = "https://euw1.api.riotgames.com/lol/match/v3/matches/" + matchId + get_token()

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        time.sleep(1)
        print("sleeping for 1 second inside get_match")
        get_match_from_account(matchId)
    else:
        print(response.status_code)
        return response.status_code
