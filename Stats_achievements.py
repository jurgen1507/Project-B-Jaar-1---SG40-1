
def playerachievements(player_achievements, ownedgames):
    appid = []
    for owned_games in ownedgames['response']['games']:
        appid.append(owned_games['appid'])

    for player_games in player_achievements:
        for AM in player_games[0]['achievements']:
            if AM['description'] == '':
                AM['description'] = 'No description available'
            player_games[0]['gameName']+':', AM['name'],'Description: '+ AM['description'] #games[0]['appid'] voor link

    games_achieved = {}
    for games_achievements in player_achievements:
        temp = []
        for AM in games_achievements[0]['achievements']:
            if AM['achieved'] == 1:
                temp.append(AM)
        games_achieved[games_achievements[0]['gameName']] = temp


    for game in games_achieved:
        for achievement in games_achieved[game]:
            achievement['name']+':', achievement['description']

if __name__ == '__main__':
    playerachievements()