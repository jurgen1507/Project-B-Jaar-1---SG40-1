import json
import urllib.request

steamAPIkey = 'FEBA5B4D2C77F02511D79C8DF42C1A57'
steamID = '76561198272503503'

response = urllib.request.urlopen(
    f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamAPIkey}&steamid={steamID}&format=json')
ownedgames = json.loads(response.read())


appid = []
for owned_games in ownedgames['response']['games']:
    appid.append(owned_games['appid'])

player_achievements = []

for app_id in appid:
    try:
        temp = []
        response = urllib.request.urlopen(f'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={app_id}&key={steamAPIkey}&steamid={steamID}&l=en')
        achievements = json.loads(response.read())
        if 'achievements' in achievements['playerstats']:
            achievements['playerstats']['appid'] = app_id
            temp.append(achievements['playerstats'])
            player_achievements.append(temp)
    except:
        pass
print(player_achievements)

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

