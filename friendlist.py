import json
steamAPIkey = 'FEBA5B4D2C77F02511D79C8DF42C1A57'
steamID = '76561198272503503'
from Merge_sort import *
def getfriendlist():
    import urllib.request

    response = urllib.request.urlopen(f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steamAPIkey}&steamid={steamID}&relationship=friend')
    friends = []
    for i in json.loads(response.read())['friendslist']['friends']:
        friends.append(i)

    friendsinfo = []
    urls = []
    for friend in friends:
        urls.append(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamAPIkey}&steamids={friend["steamid"]}')

    import threading
    import urllib.request
    import time

    start = time.time()
    online = []

    def fetch_url(url):
        urlHandler = urllib.request.urlopen(url)
        html = urlHandler.read()
        friendsinfo.append(json.loads(html)['response']['players'][0])


    threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    global friendsavatar
    friendsavatar = []
    status0 = []
    status1 = []
    status2 = []
    status3 = []
    status4 = []

    for friend in friendsinfo:
        tupe = []

        tupe.append(friend["avatar"])
        tupe.append(friend["personastate"])

        tupe = tuple(tupe)
        if friend["personastate"] == 0:
            status0.append(tupe)
        elif friend["personastate"] == 1:
            status1.append(tupe)
        elif friend["personastate"] == 2:
            status2.append(tupe)
        elif friend["personastate"] == 3:
            status3.append(tupe)
        elif friend["personastate"] == 4:
            status4.append(tupe)
    for i in status1:
        friendsavatar.append(i)
    for i in status4:
        friendsavatar.append(i)
    for i in status3:
        friendsavatar.append(i)
    for i in status2:
        friendsavatar.append(i)
    for i in status0:
        friendsavatar.append(i)

getfriendlist()