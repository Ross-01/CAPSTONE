from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (360, 640)

class EnviroDrink(MDApp):

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("settings.kv"))
        screen_manager.add_widget(Builder.load_file("about.kv"))
        return screen_manager

    # def on_start(self):
    #     Clock.schedule_once(self.login, 5)
    #
    # def login(self, *args):
    #     screen_manager.current = "login"

if __name__ == "__main__":
    EnviroDrink().run()