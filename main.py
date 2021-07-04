from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import os
import json

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def signup(self):
        self.manager.transition.direction="left"
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        print(uname, pword)
        if self.ids.username.text == "" or \
                self.ids.password.text == "":
            self.ids.wrong_creds.text = \
                "Blank username or password"
        else:
            with open('users.json') as file:
                users = json.load(file)
            print(users)
            if uname in users and \
                    users[uname]['password'] == pword:
                self.ids.username.text = ""
                self.ids.password.text = ""
                self.manager.current = 'login_success'
            else:
                self.ids.wrong_creds.text = \
                    "Invalid username or password"
                #self.ids.username.text = ""
                self.ids.password.text = ""


class SignUpScreen(Screen):
    def show_login(self):
        self.ids.username.text=""
        self.ids.password.text=""
        self.manager.transition.direction="right"
        self.manager.current="login_screen"


    def add_user(self, uname, pword):
        print(uname, pword)
        if uname=="" or pword=="":
            self.ids.umessage.text="blank username or password"
            return
        if not os.path.exists('users.json'):
            print("Users file not exists. Creating a new file....")
            with open('users.json', 'w') as file:
                users = {uname: {"username": uname, "password": pword,
                                 "created_at": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}}
                json.dump(users, file)
            print("New users file created with new user")
        else:
            print("Users file exists. Adding new user....")
            with open('users.json') as file:
                users = json.load(file)
            if uname in users:
                self.ids.umessage.text="Username already exists!!!"
                return
            with open('users.json', 'w') as file:
                users[uname] = {"username": uname, "password": pword,
                                "created_at": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
                json.dump(users, file)
            print("User added to an existing users file")
        self.manager.current = "sign_up_success"


class SignUpSccess(Screen):
    def show_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LoginSuccessScreen(Screen):
    def show_login(self):
        self.manager.transition.direction="right"
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
