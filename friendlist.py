friendsavatar = {}
from Merge_sort import sort_list
def getfriendlist(friendsinfo):
    global friendsavatar

    friendsavatar = []
    for friend in friendsinfo:

        friendsavatar.append({'steamid' : friend['response']['players'][0]["steamid"],
                               'personastate' : friend['response']['players'][0]["personastate"] * 10 if friend['response']['players'][0]["personastate"] == 1 else friend['response']['players'][0]["personastate"],
                               'avatar' : friend['response']['players'][0]["avatar"], 'username' : friend['response']['players'][0]['personaname']})

    sort_list(friendsavatar, 'personastate', 'up', 'username')


if __name__ == '__main__':
    getfriendlist()