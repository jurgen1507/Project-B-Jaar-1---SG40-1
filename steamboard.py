from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.garden.navigationdrawer import NavigationDrawer as ND
from kivy.properties import StringProperty
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty


Window.size = (700, 600)
Window.minimum_width, Window.minimum_height = 600, 400

class MainWindow(Widget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
    def ChangeGamesWindow(self):
        self.parent.ids.Navigationbar



class SteamBoardNavBar(ND, Widget):
    def __init__(self, **kwargs):
        super(SteamBoardNavBar, self).__init__(**kwargs)




class Games(RecycleView):
    games_window = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Games, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]

class SteamBoardApp(App):
    def build(self):
        
        return MainWindow()

if __name__ == '__main__':
    SteamBoardApp().run()