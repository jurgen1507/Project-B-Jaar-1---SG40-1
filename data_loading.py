import json
import dashboard_recommended
import dashboard_percentages
import friendlist
import profile_stats
import Stats_achievements
import urllib.request
import threading
from Merge_sort import *
import socket
import time
import threading
s = socket.socket()
steamAPIkey = 'E248982C26EF1A925059FD60765F8CE0'
loaded = False
ownedgames = {}
friends = {}
bans = {}
steaminfo = {}
friendsinfo = []
achievements = []
globalachievements = []
player_achievements = []
favoritegame = []
appids = []

with open('steam.json') as steamdata:
    steamjson = json.load(steamdata)


def fetch_url(url, n):
    urlHandler = urllib.request.urlopen(url)
    if n == 0:
        global ownedgames
        ownedgames = json.loads(urlHandler.read())

    if n == 1:
        global friends
        friends = json.loads(urlHandler.read())

    if n == 2:
        global bans
        bans = json.loads(urlHandler.read())
    if n == 3:
        global steaminfo
        steaminfo = json.loads(urlHandler.read())

def fetch_url2(url, n, elsevar):
    try:
        urlHandler = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        urlHandler = urllib.request.urlopen(f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={elsevar}&format=json')


    if n < len(friends['friendslist']['friends']):
        global friendsinfo
        friendsinfo.append(json.loads(urlHandler.read()))
    elif n < len(friends['friendslist']['friends']) + len(ownedgames['response']['games']):
        global achievements
        global appids
        temp = json.loads(urlHandler.read())
        try:
            if 'achievements' in temp['playerstats']:

                temp['playerstats']['appid'] = appids[n - len(friends['friendslist']['friends'])]
                achievements.append(temp)
        except:
            pass

    else:
        global globalachievements
        globalachievements.append(json.loads(urlHandler.read()))

def load_initializing_data(steamID):
    urls = []
    urls.append(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamAPIkey}&steamid={steamID}&format=json')
    urls.append(f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steamAPIkey}&steamid={steamID}&relationship=friend')
    urls.append(f'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key={steamAPIkey}&steamids={steamID}')
    urls.append(f' http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamAPIkey}&steamids={steamID}')


    threads = [threading.Thread(target=fetch_url, args=(url, n)) for n, url in enumerate(urls)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    urls = []
    global appids
    friendslist_live = []
    for friend in friends['friendslist']['friends']:
        urls.append(
            f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamAPIkey}&steamids={friend["steamid"]}')
        friendslist_live.append(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamAPIkey}&steamids={friend["steamid"]}')

    for game in ownedgames['response']['games']:
        urls.append(f'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={game["appid"]}&key={steamAPIkey}&steamid={steamID}&l=en')
        appids.append(game["appid"])

    global favoritegame
    for x in ownedgames['response']['games']:
        temp = {}
        temp['playtime'] = x['playtime_forever']
        temp['appid'] = x['appid']
        favoritegame.append(temp)

    newlist = sort_list(favoritegame, 'playtime', 'down', 'appid')
    elsevar = list(newlist)[1]["appid"]
    urls.append(f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={list(newlist)[0]["appid"]}&format=json')

    threads = [threading.Thread(target=fetch_url2, args=(url, n, elsevar)) for n, url in enumerate(urls)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    global player_achievements



    dashboard_percentages.achievement_percentage(globalachievements)
    dashboard_recommended.dashboard_recommended(steamjson, ownedgames)
    friendlist.getfriendlist(friendsinfo)
    profile_stats.profilestats(steamjson, ownedgames, friends, bans, steaminfo)
    Stats_achievements.playerachievements(achievements, ownedgames)
    # try:
    #     global s
    #     host = '192.168.1.139'  # ip of raspberry pi
    #     port = 12345
    #     s.connect((host, port))
    #     receivedatathread = threading.Thread(target=receive_data)
    #     receivedatathread.start()
    #     send_data(f'{int(dashboard_percentages.total_percentage/10)}, {int(friendlist.a[0])}, {int(friendlist.a[1])}, {int(friendlist.a[2])}, {int(friendlist.a[3])}')
    # except:
    #     pass
    live_data_thread = threading.Thread(target=load_live_data, args=(friendslist_live,))
    live_data_thread.start()


def load_live_data(friendlist_live):
    import time

    while True:
        friendsinfo = []
        def fetch_url_live(url):
            try:
                urlHandler = urllib.request.urlopen(url)
                friendsinfo.append(json.loads(urlHandler.read()))
            except:
                pass
        threads = [threading.Thread(target=fetch_url_live, args=(url,)) for url in friendlist_live]
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        friendlist.getfriendlist(friendsinfo)


def send_data(data):
    s.send(data.encode())



def receive_data():
    try:
        while True:
            data = s.recv(1024).decode()
            if data == 'FLASHBANG':
                import steamboard
                steamboard.logout()
            time.sleep(1)

    except:
        pass


if __name__ == '__main__':
    load_initializing_data('76561198272503503')