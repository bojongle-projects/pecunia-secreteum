

from mimetypes import init
import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.behaviors import CompoundSelectionBehavior
from kivy.uix.behaviors import DragBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.behaviors import CompoundSelectionBehavior
from kivy.uix.widget import Widget


class Signupgrid(GridLayout):
    def __init__(self, **kwargs):
        super(Signupgrid, self).__init__(**kwargs)
        self.cols = 2 #change column number here
        self.rows = 5 #change row number here
        self.add_widget(Label(text="Welcome to Aphrodite!"))
        self.add_widget(Label(text="Please enter your username and password below."))

        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        
        self.add_widget(Label(text="Private key:"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)



class SigunupgridApp(App):
    def build(self):
        return Signupgrid()



if __name__=="__main__":
    SigunupgridApp().run()
