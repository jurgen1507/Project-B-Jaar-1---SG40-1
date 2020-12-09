from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class RootWidget(Widget):
    pass



class SteamBoardApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    SteamBoardApp().run()