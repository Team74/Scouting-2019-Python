# pylint: disable=no-name-in-module
# pylint: disable=import-error

from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

from robot.Robot import Robot
from screens.ColorWidgets import ColorButton, ColorLabel, Colors

class LoginScreen(StackLayout):
    def __init__(self, switcher):
        super(LoginScreen, self).__init__()
        self.switcher = switcher
        self.lastScouter = ""
    
    def display(self):
        displist = []
        
        
        # row 1
        scouterDisp = ColorLabel("Scouter", (.5, .25), Colors.GREEN)
        displist.append(scouterDisp)
        
        self.scouterInput = TextInput(text=str(self.lastScouter), multiline=False, size_hint=(.5, .25))
        displist.append(self.scouterInput)

        # row 2
        teamDisp = ColorLabel("Team", (.5, .25), Colors.GREEN)
        displist.append(teamDisp)

        self.teamInput = TextInput(text="", multiline=False, size_hint=(.5, .25))
        displist.append(self.teamInput)

        # row 3
        roundDisp = ColorLabel("Round", (.5, .25), Colors.GREEN)
        displist.append(roundDisp)

        self.roundInput = TextInput(text="1", multiline=False, size_hint=(.25, .25))
        displist.append(self.roundInput)

        roundDec = ColorButton("-", (.125, .25), Colors.GREEN)
        roundDec.bind(on_release=lambda x: self.changeRound(-1))
        displist.append(roundDec)

        roundInc = ColorButton("+", (.125, .25), Colors.GREEN)
        roundInc.bind(on_release=lambda x: self.changeRound(1))
        displist.append(roundInc)
    
        # row 4
        goButton = ColorButton("GO", (1, .25), Colors.GREEN)
        
        goButton.bind(on_release=self.switchToScoring)
        displist.append(goButton)
        
        self.clear_widgets()
        for widg in displist:
            self.add_widget(widg)
    
    
    def switchToScoring(self, _):
        passedChecks = True
        if self.teamInput.text == "":
            self.teamInput.hint_text = "Enter a team number here."
            passedChecks = False
        if self.roundInput.text == "":
            self.roundInput.hint_text = "Enter a round number here."
            passedChecks = False
        if self.scouterInput.text == "":
            self.scouterInput.hint_text = "Enter your name here."
            passedChecks = False
        if not passedChecks: return
        teamNum = int("".join(char for char in self.teamInput.text if char in "1234567890"))
        roundNum = int("".join(char for char in self.roundInput.text if char in "1234567890"))
        scouterName = self.scouterInput.text
        self.switcher.robot = Robot(teamNum, roundNum, scouterName)
        self.switcher.switch("scoring")

    def changeRound(self, change):
        """
            Change the round by a number value.
            """
        if not self.roundInput.text: return
        for i in self.roundInput.text:
            if not i in "1234567890":
                return
        roundNum = int(self.roundInput.text) + change
        if roundNum <= 0:
            roundNum = 1
        self.roundInput.text = str(roundNum)

