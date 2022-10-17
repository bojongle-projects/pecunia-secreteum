


from concurrent.futures import process
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
from subprocess import Popen, PIPE















class HomeBox(BoxLayout):
    def __init__(self):
        super(HomeBox, self).__init__()
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.cols = 2
        self.rows = 4
        
        #title
        self.add_widget(Label(text='Welcome to Aphrodite', font_size=30))
        self.add_widget(Label(text='Please login or sign up below', font_size=10))
        
        #login button
        self.LoginButton = (Button(text='Login to your account')) #, process=Popen(['python3', 'login.py'], stdout=PIPE, stderr=PIPE)))
        self.add_widget(self.LoginButton)
        

        #signup button
        self.SignupButton = (Button(text='Sign up for an account')) #, process=Popen(['python3', 'signup.py'], stdout=PIPE, stderr=PIPE)))
        
        self.add_widget(self.SignupButton)

        

        #bottom text
        self.add_widget(Label(text='Take your health privacy into your hands!', font_size=20))
        self.add_widget(Label(text='Aphrodite is a free, open source, and secure way to store your health data.', font_size=10))
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.add_widget(HomeBox())
        self.name = 'home'




class SignupBox(BoxLayout):
    def __init__(self):
        super(SignupBox, self).__init__(self.SignupButton)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.cols = 2
        self.rows = 4

        #title
        self.add_widget(Label(text='Welcome to Aphrodite', font_size=30))
        self.add_widget(Label(text='Please enter your username and password below', font_size=10))

        #username
        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        #password
        self.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        #signup button
        self.SignupButton = Button(text='Sign up')
        self.add_widget(self.SignupButton)

        #login button
        self.add_widget(Button(text='Login to your account'))
        #self.LoginButton = ButtonBehavior(command = LoginScreen())
        self.add_widget(LoginBox.LoginButton)

        #login button

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super(SignupScreen, self).__init__(**kwargs)
        self.add_widget(SignupBox())
        self.name = 'signup'

       

class MainApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen())
        self.sm.add_widget(LoginScreen())
        self.sm.add_widget(SignupScreen())
        return self.sm
class LoginBox(BoxLayout):

    def __init__(self):
        super(LoginBox, self).__init__(self.LoginScreen)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.cols = 2
        self.rows = 4

        #title
        self.add_widget(Label(text='Welcome back to Aphrodite', font_size=30))
        self.add_widget(Label(text='Please enter your username and password below', font_size=10))

        #username
        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        #password
        self.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        #login button
        self.LoginButton = Button(text='Login')
        self.add_widget(self.LoginButton)

        #signup button
        self.add_widget(Button(text='Sign up for an account'))
        #self.SignupButton = ButtonBehavior(command = SignupScreen())
        self.add_widget(SignupBox.SignupButton)

    
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.add_widget(LoginBox())
        self.name = 'login'




class AphroditeApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen())
        self.sm.add_widget(LoginScreen())
        self.sm.add_widget(SignupScreen())
        return self.sm
    

         

if __name__ == '__main__':
    AphroditeApp().run()