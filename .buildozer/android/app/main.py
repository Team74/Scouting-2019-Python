# pylint: disable=no-name-in-module
# pylint: disable=import-error

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from screens.LoginScreen import LoginScreen
from screens.ScoringScreen import ScoringScreen
from screens.ClimbScreen import ClimbScreen
from robot.Robot import Robot

class ScoutingApp(App):
    def build(self):
        display = MainDisplay()
        return display

class MainDisplay(BoxLayout):
    """
        Holds an instance of each screens and switches between them.
        Also holds an instance of a robot that is shared between each screen.
        """
    def __init__(self):
        super(MainDisplay, self).__init__()
        self.screens = {
            "login": LoginScreen(self),
            "scoring": ScoringScreen(self),
            "climb": ClimbScreen(self)
        }
        self.robot = Robot(0, 0, "")
        self.currentScreen = self.screens["login"]
        self.display()

    def display(self):
        """
            Display the currently selected screen.
            """
        self.clear_widgets()
        self.add_widget(self.currentScreen)
        self.currentScreen.display()

    def switch(self, target):
        """
            Switch the current screen and display it.
            """
        self.currentScreen = self.screens[target]
        self.display()

if __name__ == "__main__":
    app = ScoutingApp()
    try:
        app.run()
    except Exception as error:
        raise error
