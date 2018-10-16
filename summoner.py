
class Summoner:

    def __init__(self, name, totalWins, totalLosses, winRatio):
        self.name = name
        self.totalWins = totalWins
        self.totalLosses = totalLosses
        self.winRatio = winRatio

    def get_summoner_name(self):
        return self.name

    def get_totalWins(self):
        return self.totalWins

    def get_totalLosses(self):
        return self.totalLosses

    def get_winRatio(self):
        return self.winRatio

    def get_summoner(self):
        print("Summoner: {0} won {1} games and lost {2} games - win ratio = {3}"
              .format(self.name, self.totalWins, self.totalLosses, self.winRatio))

    # def get_summoer_accountId(self):
    #     return self.accountId
    #
    # team1win = False
    # team2win = False
    # for teams in m['teams']:
    #     if teams['teamId'] == 100:
    #         print("team 0 heeft gewonnen: {0}".format(teams['wins']))
