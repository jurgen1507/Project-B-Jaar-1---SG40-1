friendsavatar = []
def getfriendlist(friendsinfo):
    global friendsavatar
    status0 = []
    status1 = []
    status2 = []
    status3 = []
    status4 = []

    for friend in friendsinfo:
        tupe = []
        tupe.append(friend['response']['players'][0]["avatar"])
        tupe.append(friend['response']['players'][0]["personastate"])
        tupe = tuple(tupe)
        if friend['response']['players'][0]["personastate"] == 0:
            status0.append(tupe)
        elif friend['response']['players'][0]["personastate"] == 1:
            status1.append(tupe)
        elif friend['response']['players'][0]["personastate"] == 2:
            status2.append(tupe)
        elif friend['response']['players'][0]["personastate"] == 3:
            status3.append(tupe)
        elif friend['response']['players'][0]["personastate"] == 4:
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

if __name__ == '__main__':
    getfriendlist()