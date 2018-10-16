import time

from const import get_token
from summonerService import *
from matchService import *
from summoner import *
from flask import Flask, render_template
app = Flask(__name__)
summoners = []

def print_win_ratio(summoner):
    totalGames = summoner['totalWins'] + summoner['totallosses']
    if totalGames > 1:
        if not summoner['totallosses'] == 0:
            winratio = (totalGames / summoner['totallosses']) * 10
        else:
            winratio = 100

        new_summoner = Summoner(name=summoner['summonerName'],
                                totalWins=summoner['totalWins'],
                                totalLosses=summoner['totallosses'],
                                winRatio=winratio)

        #add summoner to list
        summoners.append(new_summoner)

        #print summoner
        new_summoner.get_summoner()



        # print("{0} won {1} and lost {2} games with you - with a {3} win ratio"
        #       .format(summoner['summonerName'], summoner['totalWins'], summoner['totallosses'], winratio) )

    

def online_calculator(summonerName):
    arrayMatch = {}
    arrayMatch['match'] = []
    summoner = get_summoner_by_name(summonerName)
    print(summoner['accountId'])

    print("getting match his")
    jsonObjectMatches = get_matches_from_accountId(str(summoner['accountId']))
    for match in jsonObjectMatches['matches']:
        jsonObjectMatch = get_match_from_account(str(match['gameId']))
        arrayMatch['match'].append(jsonObjectMatch)

    print(len(arrayMatch))
    print(arrayMatch)
    save_file(arrayMatch)

def offline_calculator(summonerName):
    # summoner = get_summoner_by_name(summonerName)
    # accountId = summoner['accountId']
    accountId = 21855707
    # print(summoner['accountId'])

    arrayMatch = {}
    arrayMatch['match'] = []
    arrayPlayers = {}
    arrayPlayers['players'] = []

    arrayMatch = open_file()


    for m in arrayMatch['match']:
        team1 = False
        team2 = False

        for teams in m['teams']:
            print("teamId: {0} won: {1}".format(teams['teamId'] ,teams['win']))
            if 100 == teams['teamId']:
                team1 = teams['win']
            elif 200 == teams['teamId']:
                team2 = teams['win']
            else:
                print("Niks geselecteerd")

        for p in m['participantIdentities']:
            # print(p['player']['summonerName'] + " partId: " + str(p['participantId']))
            for participants in m['participants']:
                if p['participantId'] ==participants['participantId']:
                    print("participantId: {0}, accountId: {1}, name: {2}, teamId: {3}"
                          .format(participants['participantId'], p['player']['accountId'],
                                  p['player']['summonerName'], participants['teamId']))

                    victory: False
                    player = p['player']['summonerName']

                    if 100 == participants['teamId']:
                        victory = team1
                    elif 200 == participants['teamId']:
                        victory = team2
                    else:
                        print("Niks geselecteerd")

                    arrayPlayers['players'].append({
                        'accountId': p['player']['accountId'],
                        'summonerName': p['player']['summonerName'],
                        'teamId': participants['teamId'],
                        'won': victory
                    })

    arrayPlayersWin = {}
    arrayPlayersWin['players'] = []

    # arrayPlayersWin['players'].append({
    #     'accountId': 123,
    #     'summonerName': 'dd',
    #     'totalWins': 0,
    #     'totallosses': 0
    # })

    for p in arrayPlayers['players']:
        doesPlayerAlreadyExists = False
        foundIndex = 0

        if len(arrayPlayersWin['players']) == 0:
            print('adding account')
            arrayPlayersWin['players'].append({
                'accountId': p['accountId'],
                'summonerName': p['summonerName'],
                'totalWins': 0,
                'totallosses': 0
            })

        for playerWins in arrayPlayersWin['players']:

            if playerWins['accountId'] == p['accountId']:
                # print('Already Excists')
                doesPlayerAlreadyExists = True
                foundIndex = arrayPlayersWin['players'].index(playerWins)
                print(foundIndex)

        if doesPlayerAlreadyExists:

            print("Found player in arraylist: {0}", arrayPlayersWin['players'][foundIndex])
            if p['won'].lower() == 'win':
                print(p['won'].lower())
                print("He won this game")
                arrayPlayersWin['players'][foundIndex]['totalWins'] += 1
            elif p['won'].lower() == 'fail':
                print(p['won'])
                print("He lost this game")
                arrayPlayersWin['players'][foundIndex]['totallosses'] += 1

        else:
            # print('adding account new')
            # arrayPlayersWin['players'].append({
            #     'accountId': 4321,
            #     'summonerName': 'dd',
            #     'totalWins': 0,
            #     'totallosses': 0
            # })
            arrayPlayersWin['players'].append({
                'accountId': p['accountId'],
                'summonerName': p['summonerName'],
                'totalWins': 0,
                'totallosses': 0
            })


        # arrayPlayersWin['players'].append({
        #     'accountId': p['accountId'],
        #     'summonerName': p['summonerName'],
        #     'totalWins': 0,
        #     'totallosses': 0
        # })

    # print(arrayPlayersWin)
    for player in arrayPlayersWin['players']:
        print_win_ratio(player)

def save_file(arrayList):
    try:
        with open('matchesInfo.txt', 'w') as f:
            json.dump(arrayList, f)
    except Exception as e:
        print("Could not save file")
        print(str(e))

def open_file():
    with open('matchesInfo.txt') as json_file:
        data = json.load(json_file)
    return data

try:


    summonerName = "Drabzes"
    sumId = "21855707"

    # online_calculator(summonerName)
    offline_calculator(summonerName)

    # summoner = get_summoner_by_name(summonerName)
    # print(summoner['accountId'])
    #
    # print("getting match his")
    # jsonObjectMatches = get_matches_from_accountId(str(summoner['accountId']))
    # for match in jsonObjectMatches['matches']:
    #     jsonObjectMatch = get_match_from_account(str(match['gameId']))
    #     arrayMatch.append(jsonObjectMatch)
    #
    # print(len(arrayMatch))
    # print(arrayMatch)

    @app.route("/", methods=["GET"])
    def getCalculatorPage():
        return render_template("index.html", summoners=summoners)

    if __name__ == "__main__":
        app.run()

except Exception as e:
    print("error")
    print(str(e))



