import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

sm = ScreenManager()

for i in range(10):
    screen = Screen(name='Screen %d' % i)
    sm.add_widget(screen)

sm.current = 'Screen 5'


class HomeBox(App):
    def build(self):
        return sm

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Screen 1'))
        self.name = 'login'
    
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Screen 0'))
        self.name = 'home'

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super(SignupScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Screen 2'))
        self.name = 'signup'

class MainApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen())
        self.sm.add_widget(LoginScreen())
        self.sm.add_widget(SignupScreen())
        return self.sm
        