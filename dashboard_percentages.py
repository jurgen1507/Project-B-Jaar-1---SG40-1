import json
import urllib.request

steamAPIkey = 'FEBA5B4D2C77F02511D79C8DF42C1A57'
steamID = '76561198272503503'

response = urllib.request.urlopen(
    f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamAPIkey}&steamid={steamID}&format=json')

ownedgames = json.loads(response.read())
appid = []
from Merge_sort import *
def achievement_percentage():
    for x in ownedgames['response']['games']:
        temp = {}
        temp['playtime'] = x['playtime_forever']
        temp['appid'] = x['appid']
        appid.append(temp)


    newlist = sort_list(appid, 'playtime', 'down', 'appid')
    print(list(newlist))
    try:
        response = urllib.request.urlopen(
            f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={list(newlist)[0]["appid"]}&format=json')
        achievements = json.loads(response.read())

    except:
        response = urllib.request.urlopen(
            f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={list(newlist)[1]["appid"]}&format=json')
        achievements = json.loads(response.read())
    percentage = []
    for x in achievements['achievementpercentages']['achievements']:
        percentage.append(x['percent'])

    global total_percentage
    total_percentage = sum(percentage) / len(percentage)
    global total_percentage_angle
    total_percentage_angle = total_percentage * 3.6

achievement_percentage()







