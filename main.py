from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from datetime import datetime
import os
import json


Builder.load_file("design.kv")


class LoginScreen(Screen):
    def signup(self):
        self.manager.current="sign_up_screen"



class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        print(uname, pword)
        if not os.path.exists('users.json'):
            print("Users file not exists. Creating a new file....")
            with open('users.json', 'w') as file:
                users = {uname:{"username":uname,"password":pword,
                                "created_at":datetime.now().strftime("%Y-%m-%d %H-%M-%S")}}
                json.dump(users,file)
            print("New users file created with new user")
        else:
            print("Users file exists. Adding new user....")
            with open('users.json') as file:
                users=json.load(file)
            with open('users.json', 'w') as file:
                users[uname] = {"username":uname,"password":pword,
                                "created_at":datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
                json.dump(users,file)
            print("User added to an existing users file")




class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()