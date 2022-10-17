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






class LoginBox(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginBox, self).__init__()
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.cols = 2
        self.rows = 4
        self.add_widget(Label(text='Login to your account', font_size=30))
        self.add_widget(Label(text='Please enter your username and password below', font_size=10))
        self.add_widget(Label(text='Username'))
        self.add_widget(TextInput())
        self.add_widget(Label(text='Private Key'))
        self.add_widget(TextInput())
        self.add_widget(Button(text='Login'))
        self.add_widget(Button(text='Cancel'))
        self.add_widget(Label(text='Forgot your password?'))
        self.add_widget(Button(text='Reset Password'))
        self.add_widget(Label(text='Don\'t have an account?'))
        self.add_widget(Button(text='Sign up for an account'))
        self.add_widget(Label(text=''))
        self.add_widget(Button(text='Back to home page'))
        self.add_widget(Label(text=''))

        

class LoginApp(App):
    def build(self):
        return LoginBox()

if __name__ == '__main__':
    LoginApp().run()
