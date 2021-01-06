import urllib.request
import json
from Merge_sort import sort_list
with open('steam.json') as steamdata:
    steamjson = json.load(steamdata)


def dashboard_recommended():
    global games
    steamAPIkey = 'FEBA5B4D2C77F02511D79C8DF42C1A57'
    steamID = '76561198272503503'
    response = urllib.request.urlopen(
        f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamAPIkey}&steamid={steamID}&format=json')

    ownedgames = json.loads(response.read())
    appids = []
    for game in ownedgames['response']['games']:
        appids.append(game['appid'])

    categories = []
    for appid in appids:
        for game in steamjson:
            if appid == game['appid']:
                for i in game['genres'].split(';'):
                    categories.append(i)


    favoritegenre = dict((i, categories.count(i)) for i in categories)
    a = list(sorted(favoritegenre.items(), key=lambda item: item[1], reverse=True))
    gameslist = []
    for game in steamjson:
        if game['positive_ratings'] + game['negative_ratings'] > 60000:
            temp = []
            temp.append(game["name"])
            temp.append(game["positive_ratings"]/(game["positive_ratings"] + game["negative_ratings"]))
            temp.append(game["price"])
            temp.append(game["genres"])
            temp.append(game["appid"])
            temp.append(f'http://cdn.akamai.steamstatic.com/steam/apps/{game["appid"]}/header.jpg')
            gameslist.append(temp)

    gameslist.sort(key=lambda x: x[1], reverse=True)

    found1 = False
    games = []
    counter = 0

    for i in gameslist:
        if a[0][0] in i[3]:
            if i[4] not in appids:
                games.append(i)
                gameslist.remove(i)
                counter +=1
                if counter == 3:
                    counter = 0
                    break


    for i in gameslist:
        if a[1][0] in i[3]:
            if i[4] not in appids:
                games.append(i)
                gameslist.remove(i)
                counter += 1
                if counter == 3:
                    counter = 0
                    break


    for i in gameslist:
        if a[2][0] in i[3]:
            if i[4] not in appids:
                games.append(i)
                gameslist.remove(i)
                counter += 1
                if counter == 3:
                    counter = 0
                    break


dashboard_recommended()