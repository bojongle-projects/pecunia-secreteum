

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







class LoginBox(BoxLayout):
    def __init__(LoginButton, **kwargs):
        super(LoginButton).__init__()
        LoginBox.orientation = 'vertical'
        LoginBox.padding = 10
        LoginBox.spacing = 10
        LoginBox.cols = 2
        LoginBox.rows = 4
        LoginBox.add_widget(Label(text='Login to your account', font_size=30))
        LoginBox.add_widget(Label(text='Please enter your username and password below', font_size=10))
        LoginBox.add_widget(Label(text='Username'))
        LoginBox.add_widget(TextInput())
        LoginBox.add_widget(Label(text='Password'))
        LoginBox.add_widget(TextInput())
        LoginBox.add_widget(Button(text='Login'))
        LoginBox.add_widget(Button(text='Cancel'))
        LoginBox.add_widget(Label(text='Forgot your password?'))
        LoginBox.add_widget(Button(text='Reset Password'))
        LoginBox.add_widget(Label(text='Don\'t have an account?'))
        LoginBox.add_widget(Button(text='Sign up for an account'))
        LoginBox.add_widget(Label(text=''))
        LoginBox.add_widget(Button(text='Back to home page'))
        LoginBox.add_widget(Label(text=''))
class LoginApp(App):
    def build(self):
        return LoginBox()

if __name__ == '__main__':
    LoginApp().run()

