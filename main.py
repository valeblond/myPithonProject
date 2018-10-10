from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

class MyApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if( self.lbl.text == "0" ):
            self.lbl.text = ""

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if( str(instance.text).lower() == "x" ):
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self,instance):
        self.lbl.text = str(int(eval(self.formula))) #float values - without int
        self.formula = self.lbl.text

    def new_photo(self, instance):
        i = instance.text
        fl = FloatLayout(size_hint=(1, .09375), size=(640, 60), pos=(0, 0))
        but4 = Button(text='<--Back', size_hint=(.09375, 1), pos=(0, 0))
        but5 = Button(text='Bye :D\n  Quit', size_hint=(.09375, 1), pos=(580, 0))

        if i in self.dictionary:
            self.image = self.dictionary[i]
        else:
            raise IndentationError

        self.bl.clear_widgets()
        fl.add_widget(but4)
        fl.add_widget(but5)
        self.bl.add_widget(self.image)
        self.bl.add_widget(fl)


    def build(self, instance=None):
        self.image = Image()
        self.formula = ""

        #using of different pics depend on button
        self.dictionary = {
            'Press me, please!!!':     Image(source='Ant_man.jpg', allow_stretch=True, keep_ratio=False),
            'Go and buy \nsome milk!': Image(source='Iron_man.jpg', allow_stretch=True, keep_ratio=False),
            'You\'re a cool guy :D':   Image(source='Venom.jpg', allow_stretch=True, keep_ratio=False),
        }

       # creating layouts for pics and buttons
        self.bl = BoxLayout(orientation='vertical')
        rl = RelativeLayout()
        im_hazard = Image(source='Hazard.jpg', allow_stretch=True, keep_ratio=False)
        im_san = Image(source='Sanches.jpg', allow_stretch=True, keep_ratio=False, size_hint=(.234375, 1), pos=(0, 0))
        but1 = Button(text='Press me, please!!!', size_hint=(.234375, .5), pos=(150, 120), on_press=self.new_photo)
        but2 = Button(text='Go and buy \nsome milk!', size_hint=(.234375, .5), pos=(300, 120), on_press=self.new_photo)
        but3 = Button(text='You\'re a cool guy :D', size_hint=(.3125, .5), pos=(200, 0), on_press=self.new_photo)


        self.bl.add_widget(im_hazard)
        self.bl.add_widget(rl)
        rl.add_widget(im_san)
        rl.add_widget(but1)
        rl.add_widget(but2)
        rl.add_widget(but3)


        #making calculator
        fl2 = FloatLayout(size_hint=(.296875, 1), size=(190, 240), pos=(450, 0))

        self.lbl = Label(text="0", font_size=15, halign="right", valign="center", pos=(450, 240*.6), size_hint=(1, .4), text_size=(190, 96))
        fl2.add_widget(self.lbl)

        gl = GridLayout(cols=4, spacing=2, pos=(450, 0), size_hint=(1, .6))
        gl.add_widget( Button(text="7", on_press=self.add_number) )
        gl.add_widget( Button(text="8", on_press=self.add_number) )
        gl.add_widget( Button(text="9", on_press=self.add_number) )
        gl.add_widget( Button(text="X", on_press=self.add_operation) )

        gl.add_widget( Button(text="4", on_press=self.add_number) )
        gl.add_widget( Button(text="5", on_press=self.add_number) )
        gl.add_widget( Button(text="6", on_press=self.add_number) )
        gl.add_widget( Button(text="-", on_press=self.add_operation) )

        gl.add_widget( Button(text="1", on_press=self.add_number) )
        gl.add_widget( Button(text="2", on_press=self.add_number) )
        gl.add_widget( Button(text="3", on_press=self.add_number) )
        gl.add_widget( Button(text="+", on_press=self.add_operation) )

        gl.add_widget( Button(text="/", on_press=self.add_operation) )
        gl.add_widget( Button(text="0", on_press=self.add_number) )
        gl.add_widget( Button(text=".", on_press=self.add_number) )
        gl.add_widget( Button(text="=", on_press=self.calc_result) )

        fl2.add_widget(gl)
        rl.add_widget(fl2)

        return self.bl







window = MyApp()
window.run()