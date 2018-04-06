
class Summoner:

    def __str__(self, id, accountId, name, profileIconId, revisionDate, summonerLevel):
        self.id = id
        self.accountId = accountId
        self.name = name
        self.profileIconId = profileIconId
        self.revisionDate = revisionDate
        self.summonerLevel = summonerLevel

    def get_summoner_name(self):
        return self.name

    def get_summoer_accountId(self):
        return self.accountId
    #
    # team1win = False
    # team2win = False
    # for teams in m['teams']:
    #     if teams['teamId'] == 100:
    #         print("team 0 heeft gewonnen: {0}".format(teams['wins']))
