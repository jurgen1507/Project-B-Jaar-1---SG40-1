from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.recycleview import RecycleViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from Merge_sort import *
import json
import urllib.request

Config.set('input', 'mouse', 'mouse,disable_multitouch')
Window.size = (700, 600)
Window.minimum_width, Window.minimum_height = 600, 400

steamAPIkey = 'FEBA5B4D2C77F02511D79C8DF42C1A57'
steamID = '76561198272503503'
response = urllib.request.urlopen(
    f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamAPIkey}&steamid={steamID}&format=json')

ownedgames = json.loads(response.read())
with open('steam.json') as steamdata:
    test = json.load(steamdata)
sort_list(test, 'price', 'up')
lijst_kopie = test.copy()

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


class GamesSearch(Widget):
    def search_bar(self):
        global test
        if self.ids.OwnedGamesSwitch.active:
            searched_games = []
            for term in lijst_kopie:
                for owned in ownedgames['response']['games']:
                    if term['appid'] == owned['appid']:
                        if self.ids.search.text.lower() in term['name'].lower():
                            searched_games.append(term)
            test = searched_games
            GamesKnoppen.sorting(GamesKnoppen, 'name')
        else:
            searched_games = []
            for term in lijst_kopie:
                if self.ids.search.text.lower() in term['name'].lower():
                    searched_games.append(term)
            test = searched_games
            GamesKnoppen.sorting(GamesKnoppen, 'name')


class GamesKnoppen(Widget):
    current_button = ''
    def sorting(self, button):
        if self.current_button == button:
            descending = sort_list(test, button, 'down')
            root = self.manager.ids.Games
            print(root)
            root.ids.GamesTabel.data = [
                {'name': str(x['name']), 'price': str(x['price']), 'positiveratings': str(x['positive_ratings']),
                 'negativeratings': str(x['negative_ratings']), 'releasedate': str(x['release_date'])} for x in descending]
            root.ids.GamesTabel.refresh_from_data()
            self.current_button = ''
        else:
            global ascending
            ascending = sort_list(test, button, 'up')
            root = self.manager.ids.Games
            print(root)
            root.ids.GamesTabel.data = [{'name': str(x['name']), 'price': str(x['price']), 'positiveratings': str(x['positive_ratings']),
                          'negativeratings': str(x['negative_ratings']), 'releasedate': str(x['release_date'])} for x in ascending]
            root.ids.GamesTabel.refresh_from_data()
            self.current_button = button


class GamesTabel(RecycleView):
    def __init__(self, **kwargs):
        super(GamesTabel, self).__init__(**kwargs)
        self.data = [{'name': str(x['name']), 'price': str(x['price']), 'positiveratings': str(x['positive_ratings']),
              'negativeratings': str(x['negative_ratings']), 'releasedate': str(x['release_date'])} for x in test]



class CustomScreen(Screen):
    pass

class Games(Screen):
    pass
class Stats(Screen):
    pass

class Home(Screen):
    pass

class Profile(Screen):
    pass

class Settings(Screen):
    pass

root = ScreenManager(transition=NoTransition())

class ScreenManagerApp(App):
    def build(self):

        root.add_widget(Games(name='Games'))
        root.add_widget(CustomScreen(name='CustomScreen'))
        root.add_widget(Home(name='Home'))
        root.add_widget(Profile(name='Profile'))
        root.add_widget(Settings(name='Settings'))
        root.add_widget(Stats(name='Stats'))

        return root


if __name__ == '__main__':
    ScreenManagerApp().run()