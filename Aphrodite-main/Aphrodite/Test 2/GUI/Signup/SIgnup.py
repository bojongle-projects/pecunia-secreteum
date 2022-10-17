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



class SignupBox(BoxLayout):
    def __init__(SignupButton, **kwargs):
        super(SignupButton).__init__()
        SignupBox.orientation = 'vertical'
        SignupBox.padding = 10
        SignupBox.spacing = 10
        SignupBox.cols = 2
        SignupBox.rows = 4
        SignupBox.add_widget(Label(text='Sign up for an account', font_size=30))
        SignupBox.add_widget(Label(text='Please enter your username and password below', font_size=10))
        SignupBox.add_widget(Label(text='Username'))
        SignupBox.add_widget(TextInput())
        SignupBox.add_widget(Label(text='Password'))
        SignupBox.add_widget(TextInput())
        SignupBox.add_widget(Button(text='Sign up'))
        SignupBox.add_widget(Button(text='Cancel'))
        SignupBox.add_widget(Label(text='Forgot your password?'))
        SignupBox.add_widget(Button(text='Reset Password'))
        SignupBox.add_widget(Label(text='Already have an account?'))
        SignupBox.add_widget(Button(text='Login to your account'))
        SignupBox.add_widget(Label(text=''))
        SignupBox.add_widget(Button(text='Back to home page'))
        SignupBox.add_widget(Label(text=''))


        
class SignupApp(App):
    def build(self):
        return SignupBox()

if __name__ == '__main__':
    SignupApp().run()