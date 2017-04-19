import os

import kivy.app
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<HelloWorldScreen>:
    BoxLayout:
        Label:
            text: 'Ola Mundo'
        Button:
            text: 'Sair'
            on_press:
                self.parent.parent.quit()

""")


class HelloWorldScreen(Screen):

    def quit(self):
        """Switch back to the loader screen."""
        app = kivy.app.App.get_running_app()
        landing_screen = app.reset_landing_screen()
        self.manager.switch_to(landing_screen)

def run():
    return HelloWorldScreen()
