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


       

class loginpage(Screen):
    def __init__(self, **kwargs):
        super(loginpage, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='Login to your account', font_size=30))
        self.layout.add_widget(Label(text='Please enter your username and password below', font_size=10))
        self.layout.add_widget(Label(text='Username'))
        self.layout.add_widget(TextInput())
        self.layout.add_widget(Label(text='Password'))
        self.layout.add_widget(TextInput())
        self.layout.add_widget(Button(text='Login'))
        self.layout.add_widget(Button(text='Cancel'))
        self.layout.add_widget(Label(text='Forgot your password?'))
        self.layout.add_widget(Button(text='Reset Password'))
        self.layout.add_widget(Label(text='Don\'t have an account?'))
        self.layout.add_widget(Button(text='Sign up for an account'))
        self.layout.add_widget(Label(text=''))
        self.layout.add_widget(Button(text='Back to home page'))
        self.layout.add_widget(Label(text=''))
        self.add_widget(self.layout)




class signuppage(Screen):
    def __init__(self, **kwargs):
        super(signuppage, self).__init__(**kwargs)


        #set the layout, and make the orentation vertical    
        self.layout = BoxLayout(orientation='vertical')

        #add the widgets to the layout

        #make a label to display the sign up page title
        self.layout.add_widget(Label(text='Sign up for an account', font_size=30))
        
        #prompt for details with a label
        self.layout.add_widget(Label(text='Please enter your details below', font_size=10))
        
        #label the username text input
        self.layout.add_widget(Label(text='Username'))
        
        #add the username text input
        self.layout.add_widget(TextInput())
        
        #label the password text input
        self.layout.add_widget(Label(text='Password'))
        
        #add the password text input
        self.layout.add_widget(TextInput())
        
        #label the confirm password text input
        self.layout.add_widget(Label(text='Confirm Password'))
        
        #add the confirm password text input
        self.layout.add_widget(TextInput())
        
        #label the email text input
        self.layout.add_widget(Label(text='Email'))
        
        #add the email text input
        self.layout.add_widget(TextInput())
        
        #label the confirm email text input
        self.layout.add_widget(Label(text='Confirm Email'))
        
        #add the confirm email text input      
        self.layout.add_widget(TextInput())
       





       #define the sign up button
        self.FinishSignup = (Button(text='Sign up'))
        #add the sign up button
        self.layout.add_widget(self.FinishSignup)
        
        
        #add the cancel button
        self.layout.add_widget(Button(text='Cancel'))


        #create a label to offer the user a link to the login page
        self.layout.add_widget(Label(text='Already have an account?'))
        
        #add a buttton to direct to the login page
        self.Loginpage = Button(text='Login to your account')
        self.layout.add_widget(self.Loginpage)

    
        self.layout.add_widget(Label(text=''))
        self.layout.add_widget(Button(text='Back to home page'))
        self.layout.add_widget(Label(text=''))
        self.add_widget(self.layout)


#give the sign up button a function
    def finishsignup(self):
        print('finishsignup')
        pass












class resetpasswordpage(Screen):
    def __init__(self, **kwargs):
        super(resetpasswordpage, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='Reset your password', font_size=30))
        self.layout.add_widget(Label(text='Please enter your username and email below', font_size=10))
        self.layout.add_widget(Label(text='Username'))
        self.layout.add_widget(TextInput())
        self.layout.add_widget(Label(text='Email'))
        self.layout.add_widget(TextInput())
        self.layout.add_widget(Button(text='Reset Password'))
        self.layout.add_widget(Button(text='Cancel'))
        self.layout.add_widget(Label(text='Already have an account?'))
        self.layout.add_widget(Button(text='Login to your account'))
        self.layout.add_widget(Label(text=''))
        self.layout.add_widget(Button(text='Back to home page'))
        self.layout.add_widget(Label(text=''))
        self.add_widget(self.layout)

class homepage(Screen):
    def __init__(self, **kwargs):
        super(homepage, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='Welcome to the home page', font_size=30))
        self.layout.add_widget(Label(text='Please select an option below', font_size=10))
        self.layout.add_widget(Button(text='Login'))
        self.layout.add_widget(Button(text='Sign up'))
        self.layout.add_widget(Button(text='Forgot your password?'))
       
        self.add_widget(self.layout)

class ScreenManagement(ScreenManager):
    pass

class AphroditeApp(App):
    def build(self):
        sm = ScreenManager()
        for i in range(4):
            
            
            sm.add_widget(homepage(name='mainpageScreen %d' % i))
            sm.add_widget(loginpage(name='loginpageScreen %d' % i))
            sm.add_widget(signuppage(name='signuppageScreen %d'%i))
            sm.add_widget(resetpasswordpage(name='resetpasswordpage %d'%i))
            return sm

        

if __name__ == '__main__':
    AphroditeApp().run()
    


