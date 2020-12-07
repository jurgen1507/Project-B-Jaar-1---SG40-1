import urllib.request
import json

a = urllib.request.urlopen('http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=FEBA5B4D2C77F02511D79C8DF42C1A57&steamid=76561198272503503&format=json')
print(json.load(a))