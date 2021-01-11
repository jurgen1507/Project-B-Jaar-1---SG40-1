def profilestats(steamjson, ownedgames, friends, bans, steaminfo):
    appids = []
    for game in ownedgames['response']['games']:
        appids.append(game['appid'])

    global profilepic
    profilepic = steaminfo['response']['players'][0]['avatarfull']
    global steamid
    steamid = steaminfo['response']['players'][0]['steamid']
    global username
    username = steaminfo['response']['players'][0]['personaname']

    global friends_amount
    friends_amount = len(friends['friendslist']['friends'])
    global money_wasted
    money_wasted = 0
    for game in steamjson:
        for appid in appids:
            if game['appid'] == appid:
                money_wasted = money_wasted + game['price']

    global time_wasted
    time_wasted = 0
    for game in ownedgames['response']['games']:
        time_wasted = time_wasted + game['playtime_forever']

    global games_count
    games_count = ownedgames['response']['game_count']

    global player_bans
    player_bans = bans['players'][0]['NumberOfGameBans']

if __name__ == '__main__':
    profilestats()