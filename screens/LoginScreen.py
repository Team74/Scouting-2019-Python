# pylint: disable=no-name-in-module
# pylint: disable=import-error

from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

from robot.Robot import Robot
from screens.ColorWidgets import ColorButton, ColorLabel, Colors
from export import export

class LoginScreen(StackLayout):
    def __init__(self, switcher):
        super(LoginScreen, self).__init__()
        self.switcher = switcher
        self.lastScouter = ""
        self.lastRound = 0
    
    def display(self):
        displist = []
        
        
        # row 1
        scouterDisp = ColorLabel("Scouter", (.5, .25), Colors.GREEN)
        displist.append(scouterDisp)
        
        self.scouterInput = TextInput(text=str(self.lastScouter), multiline=False, size_hint=(.5, .25), input_type='number')
        displist.append(self.scouterInput)

        # row 2
        teamDisp = ColorLabel("Team", (.5, .25), Colors.GREEN)
        displist.append(teamDisp)

        self.teamInput = TextInput(text="", multiline=False, size_hint=(.5, .25), input_type='number')
        displist.append(self.teamInput)

        # row 3
        roundDisp = ColorLabel("Round", (.5, .25), Colors.GREEN)
        displist.append(roundDisp)

        self.roundInput = TextInput(text=str(self.lastRound + 1), multiline=False, size_hint=(.25, .25))
        displist.append(self.roundInput)

        roundDec = ColorButton("-", (.125, .25), Colors.GREEN)
        roundDec.bind(on_release=lambda x: self.changeRound(-1))
        displist.append(roundDec)

        roundInc = ColorButton("+", (.125, .25), Colors.GREEN)
        roundInc.bind(on_release=lambda x: self.changeRound(1))
        displist.append(roundInc)
    
        # row 4
        exportButton = ColorButton("Export", (.25, .25), Colors.GREEN.muteNew())
        def exportCallback(_):
            exportButton.text = export()
        exportButton.bind(on_release=exportCallback)
        displist.append(exportButton)
        
        goButton = ColorButton("GO", (.75, .25), Colors.GREEN)
        goButton.bind(on_release=self.switchToScoring)
        displist.append(goButton)
        
        self.clear_widgets()
        for widg in displist:
            self.add_widget(widg)
    
    
    def switchToScoring(self, _):
        """
            Callback function for when the goButton is pressed.
            The `_` arg is a throwaway arg for the button (it's passed in when on_release triggers).
            """
        passedChecks = True
        teamNum = "".join(char for char in self.teamInput.text if char in "1234567890")
        roundNum = "".join(char for char in self.roundInput.text if char in "1234567890")
        if teamNum == "" or len(teamNum) > 4:
            self.teamInput.hint_text = "Enter a valid team number here."
            self.teamInput.text = ""
            passedChecks = False
        if roundNum == "" or len(roundNum) > 3:
            self.roundInput.hint_text = "Enter a valid round number here."
            self.roundInput.text = ""
            passedChecks = False
        if self.scouterInput.text == "" or len(self.scouterInput.text) > 40:
            self.scouterInput.hint_text = "Enter your name here. (40 chars max)"
            passedChecks = False
        if not passedChecks: return
        scouterName = self.scouterInput.text
        self.lastRound = int(roundNum)
        self.lastScouter = scouterName
        self.switcher.robot = Robot(int(teamNum), int(roundNum), scouterName)
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

