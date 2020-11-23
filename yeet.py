import json
from tkinter import *

def main():
    with open('steam.json') as steamdata:
        data = json.load(steamdata)
        a = sorted(data, key=lambda l: l['price'])
        for x in a:
            print(f'{x["name"]}, {x["price"]}')
        textVar.set(a[0]["name"])



root = Tk()

mainFrame = Frame(master=root)
mainFrame.pack()
textVar = StringVar()

textLabel = Label(master=mainFrame, textvariable=textVar)
textLabel.pack()
main()
root.mainloop()
