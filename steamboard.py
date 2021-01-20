from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
import random
from Merge_sort import sort_list
from data_loading import *
from friendlist import friendsavatar
Config.set('input', 'mouse', 'mouse,disable_multitouch')

sort_list(steamjson, 'price', 'up', 'name')
lijst_kopie = steamjson.copy()


class MainWindow(Widget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)


class LoginScreen(Screen):
    def btn(self):
        try:
            Login = self.ids.login.text.replace('https://steamcommunity.com/profiles/', '').split('/')
            load_initializing_data(Login[0])
            ScreenManagerApp.startup(ScreenManagerApp)
            self.parent.current = 'Home'
        except:
            self.error = '* Either the account has been set to private or the link provided is incorrect.'


class TitleScreen(Widget):
    def __init__(self, **kwargs):
        super(TitleScreen, self).__init__(**kwargs)
        import profile_stats
        self.profilepicture = str(profile_stats.profilepic)
        self.profilename = str(profile_stats.username)


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


class Dashboard(Widget):
    def __init__(self, **kwargs):
        from dashboard_recommended import games
        from dashboard_percentages import total_percentage_angle, total_percentage
        super(Dashboard, self).__init__(**kwargs)
        self.angle = total_percentage_angle
        self.percentage = str(round(total_percentage, 2)) + '%'
        self.game1 = games[random.randint(0,int(len(games)/3-1))]
        self.game2 = games[random.randint(int(len(games)/3),int(len(games)/3 * 2 -1 ))]
        self.game3 = games[random.randint(int(len(games)/3*2) ,len(games)-1)]


class GamesInfoPopup(Popup):
    def __init__(self, **kwargs):
        super(GamesInfoPopup, self).__init__(**kwargs)


class GamesPopup(Widget):
    def show_gamesinfo_popup(self, name, appid, categories, genres, price, steamspy, release, achievements, english, positive, developer, negative, publisher, platforms, average, required, median, owners):
        show = GamesInfoPopup()
        show.name = name
        show.appid = appid
        show.categories = categories.replace(';', ', ')
        show.genres = genres.replace(';', ', ')
        show.price = price
        show.steamspy = steamspy.replace(';', ', ')
        show.release = release
        show.achievements = achievements
        show.english = english
        show.positive = positive
        show.developer = developer
        show.negative = negative
        show.publisher = publisher
        show.percentage = str(round(int(positive) / (int(positive)+int(negative)) * 100, 2))
        show.platforms = platforms.replace(';', ', ')
        show.average = average
        show.required = required
        show.median = median
        show.owners = owners
        show.banner = f'http://cdn.akamai.steamstatic.com/steam/apps/{appid}/header.jpg'
        show.open()


class Table(BoxLayout):
    def btn(self, name, appid, categories, genres, price, steamspy, release, achievements, english, positive, developer, negative, publisher, platforms, average, required, median, owners):
        GamesPopup.show_gamesinfo_popup(GamesPopup, name, appid, categories, genres, price, steamspy, release, achievements, english, positive, developer, negative, publisher, platforms, average, required, median, owners)


class GamesKnoppen(Widget):
    current_button = ''
    def sorting(self, button, GK):
        if self.current_button == button and GK:
            descending = sort_list(steamjson, button, 'down', 'name')
            self.sortbutton = button
            self.updown = 'down'
            self.parent.ids.GT.data = [
                {'name': str(x['name']), 'price': str('{0:.2f}'.format(x['price'])), 'positiveratings': str(x['positive_ratings']),
                 'negativeratings': str(x['negative_ratings']), 'releasedate': str(x['release_date']), 'appid' : str(x['appid']),
                 'release' : str(x['release_date']),  'english': str(x['english']),  'developer': str(x['developer']),
                 'publisher': str(x['publisher']),  'platforms': str(x['platforms']),  'required': str(x['required_age']),
                 'categories': str(x['categories']),  'genres': str(x['genres']),  'steamspy': str(x['steamspy_tags']),
                 'achievements': str(x['achievements']),  'average': str(x['average_playtime']),  'median': str(x['median_playtime']),
                 'owners': str(x['owners'])} for x in descending]
            self.parent.ids.GT.refresh_from_data()
            self.current_button = ''

        else:
            global ascending
            ascending = sort_list(steamjson, button, 'up', 'name')
            self.sortbutton = button
            self.updown = 'up'
            self.parent.ids.GT.data = [{'name': str(x['name']), 'price': str('{0:.2f}'.format(x['price'])), 'positiveratings': str(x['positive_ratings']),
                 'negativeratings': str(x['negative_ratings']), 'releasedate': str(x['release_date']), 'appid' : str(x['appid']),
                 'release' : str(x['release_date']),  'english': str(x['english']),  'developer': str(x['developer']),
                 'publisher': str(x['publisher']),  'platforms': str(x['platforms']),  'required': str(x['required_age']),
                 'categories': str(x['categories']),  'genres': str(x['genres']),  'steamspy': str(x['steamspy_tags']),
                 'achievements': str(x['achievements']),  'average': str(x['average_playtime']),  'median': str(x['median_playtime']),
                 'owners': str(x['owners'])} for x in ascending]
            self.parent.ids.GT.refresh_from_data()
            self.current_button = button


class GamesSearch(Widget):
    def search_bar(self):
        global steamjson
        if self.ids.OwnedGamesSwitch.active:
            searched_games = []
            for term in lijst_kopie:
                for owned in ownedgames['response']['games']:
                    if term['appid'] == owned['appid']:
                        if self.ids.search.text.lower() in term['name'].lower():
                            searched_games.append(term)
            steamjson = searched_games
            GamesKnoppen.sorting(self.parent.ids.GK, 'name', False)
        else:
            searched_games = []
            for term in lijst_kopie:
                if self.ids.search.text.lower() in term['name'].lower():
                    searched_games.append(term)
            steamjson = searched_games
            GamesKnoppen.sorting(self.parent.ids.GK, 'name', False)


class GamesTable(RecycleView):
    def __init__(self, **kwargs):
        super(GamesTable, self).__init__(**kwargs)
        self.data = [{'name': str(x['name']), 'price': str('{0:.2f}'.format(x['price'])), 'positiveratings': str(x['positive_ratings']),
                 'negativeratings': str(x['negative_ratings']), 'releasedate': str(x['release_date']),
                 'appid' : str(x['appid']), 'release' : str(x['release_date']),  'english': str(x['english']),
                 'developer': str(x['developer']),  'publisher': str(x['publisher']),  'platforms': str(x['platforms']),
                 'required': str(x['required_age']), 'categories': str(x['categories']),  'genres': str(x['genres']),
                 'steamspy': str(x['steamspy_tags']),  'achievements': str(x['achievements']),  'average': str(x['average_playtime']),
                 'median': str(x['median_playtime']),  'owners': str(x['owners'])} for x in steamjson]


class Friendlist(RecycleView):
    friendsinfo_first = {}
    def __init__(self, **kwargs):
        super(Friendlist, self).__init__(**kwargs)
        self.data = [{'atavar': str(x["avatar"]), 'status': str('.\icons\status' +str(1 if x["personastate"] == 10 else x["personastate"])+'.png')} for x in friendsavatar]
        self.friendsinfo_first = friendsavatar
        updatethread = threading.Thread(target=self.update)
        updatethread.start()

    def update(self):
        while True:
            from friendlist import friendsavatar
            if friendsavatar != self.friendsinfo_first:
                self.data = [{'atavar': str(x["avatar"]), 'status': str('.\icons\status' +str(1 if x["personastate"] == 10 else x["personastate"])+'.png')} for x in friendsavatar]
                self.friendsinfo_first = friendsavatar
                try:
                    send_data(f'{int(total_percentage / 10)}, {int(friendlist.a[0])}, {int(friendlist.a[1])}, {int(friendlist.a[2])}, {int(friendlist.a[3])}')
                except:
                    pass
                self.refresh_from_data()
            time.sleep(5)


class Friends(Widget):
    pass


class ProfileStats(Widget):
    def __init__(self, **kwargs):
        super(ProfileStats, self).__init__(**kwargs)
        self.hours = [random.uniform(0, 10),random.uniform(0, 10),random.uniform(0, 10),random.uniform(0, 10),random.uniform(0, 10),random.uniform(0, 10),random.uniform(0, 10),]
        import profile_stats
        self.profilepic = str(profile_stats.profilepic)
        self.totalgames = str(profile_stats.games_count)
        self.moneywasted = str('{0:.2f}'.format(profile_stats.money_wasted))
        self.totalfriends = str(profile_stats.friends_amount)
        self.totalbans = str(profile_stats.player_bans)
        self.timewasted = str(round(profile_stats.time_wasted / 60))
        self.steamid = str(profile_stats.steamid)
        self.username = str(profile_stats.username)


class StatsInfoPopup(Popup):
    pass


class StatsPopup(Widget):
    def show_statsinfo_popup(self, achievementdata):
        popup = StatsInfoPopup()
        popup.gamename = eval(achievementdata)['gameName']
        AchievementsRVPopup.adddata(AchievementsRVPopup, achievementdata)
        popup.open()


class AchievementTable(BoxLayout):
    def btn(self, achievementdata):
        StatsPopup.show_statsinfo_popup(StatsPopup, achievementdata)


class AchievementsRVPopup(RecycleView):
    def __init__(self, **kwargs):
        super(AchievementsRVPopup, self).__init__(**kwargs)
    def adddata(self, data):
        self.data = [{'name' : str(x['name']), 'description': str(x['description']), 'achieved' : str(x['achieved'])} for x in eval(data)['achievements']]


class Achievements(RecycleView):
    def __init__(self, **kwargs):
        super(Achievements, self).__init__(**kwargs)
        self.data = [{'gamename':str(x["playerstats"]['gameName']), 'banner': str(f'http://cdn.akamai.steamstatic.com/steam/apps/{x["playerstats"]["appid"]}/header.jpg'), 'achievementdata' : str(x["playerstats"])} for x in achievements]


class AchievementHelp(BoxLayout):
    pass


class Games(Screen):
    pass


class Stats(Screen):
    pass


class RV(BoxLayout):
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
        self.icon = './icons/steamboardicon_small.png'
        self.title = 'SteamBoard'
        Window.size = (500,400)

        root.add_widget(LoginScreen(name='LoginScreen'))
        return root

    def startup(self):
        root.add_widget(Games(name='Games'))
        root.add_widget(Home(name='Home'))
        root.add_widget(Profile(name='Profile'))
        root.add_widget(Settings(name='Settings'))
        root.add_widget(Stats(name='Stats'))
        Window.size = (800, 600)
        Window.minimum_width, Window.minimum_height = 800, 500


def logout():
    ScreenManagerApp().stop()


if __name__ == '__main__':
    ScreenManagerApp().run()