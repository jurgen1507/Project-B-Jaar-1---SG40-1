friendsavatar = {}
a = []
from Merge_sort import sort_list

def getfriendlist(friendsinfo):
    global friendsavatar
    online = 0
    away = 0
    nodisturb = 0
    offline = 0
    friendsavatar = []
    for friend in friendsinfo:
        friendsavatar.append({'steamid' : friend['response']['players'][0]["steamid"],
                               'personastate' : friend['response']['players'][0]["personastate"] * 10 if friend['response']['players'][0]["personastate"] == 1 else friend['response']['players'][0]["personastate"],
                               'avatar' : friend['response']['players'][0]["avatar"], 'username' : friend['response']['players'][0]['personaname']})
        if friend['response']['players'][0]["personastate"]== 1:
            online += 1
        elif friend['response']['players'][0]["personastate"] == 0:
            offline += 1
        elif friend['response']['players'][0]["personastate"] == 3:
            away += 1
        elif friend['response']['players'][0]["personastate"] == 4:
            nodisturb +=1
    friendsavatar = sort_list(friendsavatar, 'personastate', 'down', 'username')
    global a
    a = []
    a.append(offline/len(friendsinfo) * 8)
    a.append(nodisturb/len(friendsinfo) * 8)
    a.append(away/len(friendsinfo) * 8)
    a.append(online/len(friendsinfo) * 8)
    from iteround import saferound
    a = saferound(a, places=0)


if __name__ == '__main__':
    getfriendlist()