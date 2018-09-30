from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
'''
from kivy.config import Config
Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '640');
Config.set('graphics', 'height', '480');
'''
class MyApp(App):
    def build(self):
        #al = AnchorLayout()
        bl = BoxLayout(orientation = 'vertical', size_hint = [.5, .5])

        bl.add_widget( TextInput())
        bl.add_widget( TextInput())
        bl.add_widget(Button(text="Войти"))

        #al.add_widget(bl)
        return bl

class FullImage(Image):
    pass

window = MyApp()
window.run()