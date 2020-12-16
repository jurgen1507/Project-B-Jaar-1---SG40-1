from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from test import *
import json
Window.size = (700, 600)
Window.minimum_width, Window.minimum_height = 600, 400


with open('steam.json') as steamdata:
    test = json.load(steamdata)
sort_list(test, 'price')

class MainWindow(Widget):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)



class Friendlist(RecycleView):
    def __init__(self, **kwargs):
        super(Friendlist, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]

class PlaceHolder(Widget):
    pass

class SteamBoardNavBar(Widget):
    foldednavbar = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(SteamBoardNavBar, self).__init__(**kwargs)
    def Fold(self):
        anim = Animation(pos=(-225, 0), t='in_out_quad', duration=0.2)
        anim.start(self)
    def UnFold(self):
        anim = Animation(pos=(0, 0), t='in_out_quad', duration=0.2)
        anim.start(self)

class Tabel(BoxLayout):
    pass
class GamesKnoppen(Widget):
    pass
class Games(RecycleView):

    def __init__(self, **kwargs):
        super(Games, self).__init__(**kwargs)

        self.data = [{'name': str(x['name']), 'price': str(x['price']), 'positiveratings': str(x['positive_ratings']),
                      'negativeratings': str(x['negative_ratings']), 'releasedate': str(x['release_date'])} for x in test]

class SteamBoardApp(App):

    def build(self):
        return MainWindow()

if __name__ == '__main__':
    SteamBoardApp().run()