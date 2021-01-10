from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current='signup_screen'
    def login(self,usname,pwd):
        with open('users.json') as file:
            users=json.load(file)
        if usname in users and users[usname]['password']==pwd:
            self.manager.current='login screen success'
        else:
            self.ids.login_wrong.text='Wrong username or password'

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, user, password):
        '''
        with open('users.json') as file:
            users=json.load(file)
        users[user]={"username": user,
                    "password": password,
                    "created": datetime.now()}

        with open('users.json','w') as file:
            json.dump(users,file)
        '''
        self.manager.current='signup_success'

class SignUpSuccessScreen(Screen):
    def go_to_home(self):
        self.manager.transition.direction='right'
        self.manager.current='login_screen'
class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction='right'
        self.manager.current='login_screen'

    def get_quotes(self,feel):
        print(feel)

        feel=feel.lower()
        available_feelings=glob.glob('quotes/*txt')
        available_feelings=[Path(filename).stem for filename in available_feelings]

        print(available_feelings)

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf8") as file:
                quotes=file.readlines()
            self.ids.quote.text=random.choice(quotes)
        else:
            self.ids.quote.text='Error, please try again'
class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    MainApp().run()
