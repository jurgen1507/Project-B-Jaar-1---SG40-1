from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.garden.navigationdrawer import NavigationDrawer as ND
from kivy.properties import StringProperty

class SteamBoardWindow(ND):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)




class SteamBoardApp(App):
    def build(self):
        return SteamBoardWindow()

if __name__ == '__main__':
    SteamBoardApp().run()