import json
import kivy
from Merge_sort import merge_sort
from tkinter import *
from operator import itemgetter
import urllib.request
with open('steam.json') as steamdata:
    data = json.load(steamdata)

steamAPIkey = 'FEBA5B4D2C77F02511D79C8DF42C1A57'
steamID = '76561198272503503'

def main(*args):
    search_term = search_var.get()
    option = optionvariable.get().lower().replace(' ', '_')
    gamelijst.delete(0, 'end')
    response = urllib.request.urlopen(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamAPIkey}&steamid={steamID}&format=json')
    ownedgames = json.loads(response.read())
    print(ownedgames)

    # Sorteert volgens de python functie sorted oplopend of aflopend
    if ascdesc.get () == 'Descending':
        merge_sort(data, 0, len(data) - 1, option)
        sortedlist = data[::-1]
    else:
        merge_sort(data, 0, len(data) - 1, option)
        sortedlist = data

    # Kijkt of het checkbutton knopje is aangekruisd, als dat zo is dan worden alleen de spellen in de speler library getoond
    if CheckVar.get() == 1:
        for i in sortedlist:
            for j in ownedgames['response']['games']:
                if i['appid'] == j['appid']:
                    if search_term.lower() in i['name'].lower():
                        gamelijst.insert(END, i['name'])
    else:
        for i in sortedlist:
            if search_term.lower() in i['name'].lower():
                gamelijst.insert(END, i['name'])
    mainFrame.update()

def getgameinfo(valuetofind):
    for i in data:
        if valuetofind == i['name']:
            return i

def callback(event):
    selection = event.widget.curselection()
    if selection:
        # Maakt de lijst weer leeg om de nieuwe informatie toe te voegen
        textLabel.delete(0, END)
        # Vraagt op welk spel is aangeklikt in de lijst met spellen
        index = selection[0]
        widgetdata = event.widget.get(index)
        game = list(getgameinfo(widgetdata).values())
        # Pakt de appid van het aangeklikte spel om zo statistieken van de speler te kunnen krijgen
        appid = game[0]
        try:
            response = urllib.request.urlopen(
                f'http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={appid}&key={steamAPIkey}&steamid={steamID}')
            player_stats = json.loads(response.read())
        # Als er geen statistieken zijn, dan gebeurt er niks
        except:
            pass

        # Voegt standaard informatie van het spel toe in de infolijst
        textLabel.insert(END,
            f'Name: {widgetdata}\n')
        textLabel.insert(END,
            f'Price: ${game[17]}\n')
        textLabel.insert(END,
            f'Positive ratings: {game[12]}\n')
        textLabel.insert(END,
            f'Negative ratings: {game[13]}\n')
        textLabel.insert(END,
            f'Release date: {game[2]}\n')
        textLabel.insert(END,
            f'Average playtime: {game[14]}\n')

        # Als er statistieken zijn, dan voegt dit het toe in de infolijst
        try:
            for i in range(len(player_stats["playerstats"]["stats"])):
                text = gameinfo.get() + f'{player_stats["playerstats"]["stats"][i]["name"].replace("_", " ")}: {player_stats["playerstats"]["stats"][i]["value"]}\n'
                textLabel.insert(END, text)
        # Als er geen statistieken zijn, print dan "No player stats"
        except:
            textLabel.insert(END, 'No Player Stats')

OptionList = [
    'Price',
    'Positive Ratings',
    'Negative Ratings',
    'Name',
    'Release Date',
    'Average Playtime',

]

root = Tk()
root.resizable(width=0, height=0)
mainFrame = Frame(root, width=600, height=400)
mainFrame.pack()
textVar = StringVar()
optionvariable = StringVar(mainFrame)
optionvariable.set(OptionList[0])
optionlist= OptionMenu(mainFrame, optionvariable, *OptionList, command=main)
optionlist.place(relx=0.075, rely=0.05, anchor=W)
ascdesclist = ['Ascending', 'Descending']
ascdesc = StringVar(mainFrame)
ascdesc.set(ascdesclist[0])
adlist= OptionMenu(mainFrame, ascdesc, *ascdesclist, command=main)
adlist.place(relx=0.3, rely=0.05, anchor=W)
sortByLabel = Label(master=mainFrame, text='Sort by: ', foreground='black')
sortByLabel.place(relx=0.05, rely=0.05, anchor=CENTER)
gamelijst = Listbox(master=mainFrame, width=30, height=20)
gamelijst.place(relx=0.03, rely=0.15, anchor=NW)
gamelijst.bind("<<ListboxSelect>>", callback)
search_var = StringVar()
search_var.trace("w", main)
searchlabel = Label(master=mainFrame, text='Search:')
searchlabel.place(relx=0.6, rely=0.05, anchor=CENTER)
searchentry = Entry(master=mainFrame, textvariable=search_var, width=13)
searchentry.place(relx=0.7, rely=0.05, anchor=CENTER)
CheckVar = IntVar()
checkbutton = Checkbutton(master=mainFrame, text='Owned Games', variable=CheckVar,onvalue=1, offvalue=0, command=main)
checkbutton.place(relx=0.9, rely=0.05, anchor=CENTER)
gameinfo = StringVar()
gameinfo.set('')
textLabel = Listbox(master=mainFrame, width=45, height=20)
textLabel.place(relx=0.35, rely=0.15, anchor=NW)
mainFrame.pack()
main()
root.mainloop()
