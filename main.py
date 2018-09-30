from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.config import Config
Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '640');
Config.set('graphics', 'height', '480');

class MyApp(App):
    def build(self):
        bl = BoxLayout(orientation = 'vertical')
        fl = FloatLayout(size=(640, 240))
        hazard = Image(source='Hazard.jpg', allow_stretch=True, keep_ratio=False)
        san = Image(source='Sanches.jpg', allow_stretch=True, keep_ratio=False, size_hint=(.234375, 1), pos=(0, 0))
        but1 = Button(text='Press me, please!!!', size_hint=(.234375, .5), pos=(150, 120))
        but2 = Button(text='Go and buy \nsome milk!', size_hint=(.234375, .5), pos=(300, 120))
        wid1 = Widget(size_hint=(.78125, .5), pos=(150, 0))
        but3 = Button(text='You\'re a cool guy :D', size_hint=(.3125, .5), pos=(200, 0))

        bl.add_widget(hazard)
        bl.add_widget(fl)
        fl.add_widget(san)
        fl.add_widget(but1)
        fl.add_widget(but2)
        fl.add_widget(wid1)
        fl.add_widget(but3)
        return bl

class FullImage(Image):
    pass

window = MyApp()
window.run()