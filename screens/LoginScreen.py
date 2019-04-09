# pylint: disable=no-name-in-module
# pylint: disable=import-error

from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

from robot.Robot import Robot
from screens.ColorWidgets import ColorButton, ColorLabel, Colors
from export import export, getMatchSchedule, getTeamsForRound

class LoginScreen(StackLayout):
    def __init__(self, switcher):
        super(LoginScreen, self).__init__()
        self.switcher = switcher
        self.lastScouter = ""
        self.lastRound = 0
        
        self.teamButtonLayout = StackLayout(size_hint=(.5, .25))
        
        self.teamRed1 = ColorButton("", (1/3, .5), Colors.FAIR_RED)
        self.teamRed1.defaultColor = Colors.FAIR_RED.muteNew().asTupleWithAlpha()
        self.teamRed2 = ColorButton("", (1/3, .5), Colors.FAIR_RED)
        self.teamRed2.defaultColor = Colors.FAIR_RED.muteNew().asTupleWithAlpha()
        self.teamRed3 = ColorButton("", (1/3, .5), Colors.FAIR_RED)
        self.teamRed3.defaultColor = Colors.FAIR_RED.muteNew().asTupleWithAlpha()
        self.teamBlue1 = ColorButton("", (1/3, .5), Colors.FAIR_BLUE)
        self.teamBlue1.defaultColor = Colors.FAIR_BLUE.muteNew().asTupleWithAlpha()
        self.teamBlue2 = ColorButton("", (1/3, .5), Colors.FAIR_BLUE)
        self.teamBlue2.defaultColor = Colors.FAIR_BLUE.muteNew().asTupleWithAlpha()
        self.teamBlue3 = ColorButton("", (1/3, .5), Colors.FAIR_BLUE)
        self.teamBlue3.defaultColor = Colors.FAIR_BLUE.muteNew().asTupleWithAlpha()
        
        self.selectedTeam = self.teamRed1
        
        self.teamRed1.bind(on_release=self.updateSelectedTeam)
        self.teamRed2.bind(on_release=self.updateSelectedTeam)
        self.teamRed3.bind(on_release=self.updateSelectedTeam)
        self.teamBlue1.bind(on_release=self.updateSelectedTeam)
        self.teamBlue2.bind(on_release=self.updateSelectedTeam)
        self.teamBlue3.bind(on_release=self.updateSelectedTeam)
        
        self.teamButtonLayout.add_widget(self.teamRed1)
        self.teamButtonLayout.add_widget(self.teamRed2)
        self.teamButtonLayout.add_widget(self.teamRed3)
        self.teamButtonLayout.add_widget(self.teamBlue1)
        self.teamButtonLayout.add_widget(self.teamBlue2)
        self.teamButtonLayout.add_widget(self.teamBlue3)
    
    def display(self):
        displist = []
        
        
        # row 1
        scouterDisp = ColorLabel("Scouter", (.5, .25), Colors.GREEN)
        displist.append(scouterDisp)
        
        self.scouterInput = TextInput(text=str(self.lastScouter), multiline=False, size_hint=(.5, .25))
        displist.append(self.scouterInput)

        # row 2
        teamDisp = ColorLabel("Team", (.3, .25), Colors.GREEN)
        displist.append(teamDisp)

        self.teamInput = TextInput(text="", multiline=False, size_hint=(.2, .25))
        displist.append(self.teamInput)
        
        displist.append(self.teamButtonLayout)

        # row 3
        roundDisp = ColorLabel("Round", (.5, .25), Colors.GREEN)
        displist.append(roundDisp)

        self.roundInput = TextInput(text=str(self.lastRound), multiline=False, size_hint=(.25, .25))
        displist.append(self.roundInput)
        self.roundInput.bind(on_text_validate=lambda _: self.setRound(self.roundInput.text))
        
        self.changeRound(1)

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
        
        downloadButton = ColorButton("Get match schedule", (.25, .25), Colors.GREEN.muteNew())
        def downloadCallback(_):
            downloadButton.text = getMatchSchedule()
        downloadButton.bind(on_release=downloadCallback)
        displist.append(downloadButton)
        
        goButton = ColorButton("GO", (.5, .25), Colors.GREEN)
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

    def updateSelectedTeam(self, teamButton):
        self.selectedTeam.background_color = self.selectedTeam.defaultColor
        self.selectedTeam = teamButton
        self.selectedTeam.background_color = Colors.GREEN.muteNew().asTupleWithAlpha()
        
        self.teamInput.text = self.selectedTeam.text

    def changeRound(self, change):
        """
            Change the round by a number value.
            """
        if not self.roundInput.text:
            self.roundInput.text = "1"
            return
        for i in self.roundInput.text:
            if not i in "1234567890":
                return
        roundNum = int(self.roundInput.text) + change
        if roundNum <= 0:
            roundNum = 1
        self.setRound(str(roundNum))
    
    def setRound(self, roundNum):
        """
            Sets the text on the roundInput button to a specific number string.
            `roundNum` is a string. If the string contains nondigit characters, nothing is done.
            """
        for i in roundNum:
            if not i in "1234567890":
                return
        self.roundInput.text = str(roundNum)
        
        teams = getTeamsForRound(roundNum)
        if teams:
            _, r1, r2, r3, b1, b2, b3 = teams
            self.teamRed1.text = str(r1)
            self.teamRed2.text = str(r2)
            self.teamRed3.text = str(r3)
            self.teamBlue1.text = str(b1)
            self.teamBlue2.text = str(b2)
            self.teamBlue3.text = str(b3)
            self.updateSelectedTeam(self.selectedTeam)
        else:
            self.teamRed1.text = ""
            self.teamRed2.text = ""
            self.teamRed3.text = ""
            self.teamBlue1.text = ""
            self.teamBlue2.text = ""
            self.teamBlue3.text = ""
        