import json
import urllib.request
steamAPIkey = 'FEBA5B4D2C77F02511D79C8DF42C1A57'
steamID = '76561198272503503'

with open('steam.json') as steamdata:
    steamjson = json.load(steamdata)

def profilestats():
    response = urllib.request.urlopen(
        f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamAPIkey}&steamid={steamID}&format=json')
    ownedgames = json.loads(response.read())

    appids = []
    for game in ownedgames['response']['games']:
        appids.append(game['appid'])
    response = urllib.request.urlopen(
        f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steamAPIkey}&steamid={steamID}&relationship=friend')
    friends = []
    for i in json.loads(response.read())['friendslist']['friends']:
        friends.append(i)
    response = urllib.request.urlopen(
        f'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key={steamAPIkey}&steamids={steamID}')
    bans = json.loads(response.read())
    response = urllib.request.urlopen(
        f' http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamAPIkey}&steamids={steamID}')
    steaminfo = json.loads(response.read())


    global profilepic
    profilepic = steaminfo['response']['players'][0]['avatarfull']
    global steamid
    steamid = steaminfo['response']['players'][0]['steamid']
    global username
    username = steaminfo['response']['players'][0]['personaname']

    global friends_amount
    friends_amount = len(friends)

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





profilestats()