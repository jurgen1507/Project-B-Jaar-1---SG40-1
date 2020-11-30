import json
from tkinter import *

with open('steam.json') as steamdata:
    data = json.load(steamdata)

sortedlist = sorted(data, key=lambda l: l['price'])

def main(*args):
    search_term = search_var.get()
    option = optionvariable.get().lower().replace(' ', '_')
    gamelijst.delete(0, 'end')
    if ascdesc.get() == 'Descending':
        sortedlist = sorted(data, key=lambda l: l[option], reverse=True)
    else:
        sortedlist = sorted(data, key=lambda l: l[option])
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
        index = selection[0]
        widgetdata = event.widget.get(index)
        game = list(getgameinfo(widgetdata).values())
        gameinfo.set(f'Name: {widgetdata}\nPrice: ${game[17]}\nPositive ratings: {game[12]}\nNegative ratings: {game[13]}\nRelease date: {game[2]}\nAverage playtime: {game[14]}')
    else:
        gameinfo.set("")

OptionList = [
    'Price',
    'Positive Ratings',
    'Negative Ratings',
    'Name',
    'Release Date',
    'Average Playtime'

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

gameinfo = StringVar()
gameinfo.set('')
textLabel = Label(master=mainFrame, textvariable=gameinfo, justify=LEFT)
textLabel.place(relx=0.35, rely=0.15)

mainFrame.pack()
main()
root.mainloop()
