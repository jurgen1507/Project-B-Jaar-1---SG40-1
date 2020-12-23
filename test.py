from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
Builder.load_string('''
<Custom@Switch>:
    values: ['OFF', 'ON']
    canvas:
        Color:
            rgb: 0, 0, 0, 0
        Rectangle:
            size: [sp(41.5), sp(20)]
            pos: [self.center_x - sp(41.5), self.center_y - sp(10)]
        Color:
            rgb: 1, 1, 1, 1
        Rectangle:
            size: [sp(41.5), sp(20)]
            pos: [self.center_x, self.center_y - sp(10)]
    Label:
        text: '[b]{}[/b]'.format(root.values[0])
        markup: True
        font_size: 13
        pos: [root.center_x - sp(70), root.center_y - sp(50)]
    Label:
        color: 1, 1, 1, 1
        text: '[b]{}[/b]'.format(root.values[1])
        markup: True
        font_size: 13
        pos: [root.center_x - sp(30), root.center_y - sp(50)]

<Test>:
    Custom:
    Switch:
    Custom:
        values: ['Yes', 'No']
''')
class Test(BoxLayout): pass
runTouchApp(Test())