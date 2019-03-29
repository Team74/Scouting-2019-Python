
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

from screens.ColorWidgets import ColorButton, ColorLabel, Colors
from robot.enums import EndingStates

class ClimbScreen(StackLayout):
    def __init__(self, switcher):
        super(ClimbScreen, self).__init__()
        self.switcher = switcher
    
    def display(self):
        displist = []
        
        leftSide = StackLayout(size_hint=(.5, 1))
        displist.append(leftSide)
        rightSide = StackLayout(size_hint=(.5, 1))
        displist.append(rightSide)
        
        # Climb layout
        climbLayout = StackLayout(size_hint=(1, .5))
        
        climbLabel = ColorLabel("Points scored for climb", (1, .2), Colors.YELLOW)
        self.climb0 = ColorButton("0", (.25, .8), Colors.DEEP_BLUE)
        self.climb3 = ColorButton("3", (.25, .8), Colors.BLUE)
        self.climb6 = ColorButton("6", (.25, .8), Colors.FAIR_BLUE)
        self.climb12 = ColorButton("12", (.25, .8), Colors.LIGHT_BLUE)
        
        def climbCallback(state):
            self.switcher.robot.endedOn = state
            self.updateClimbLayout()
        self.climb0.bind(on_release=lambda _: climbCallback(EndingStates.NONE))
        self.climb3.bind(on_release=lambda _: climbCallback(EndingStates.LOW))
        self.climb6.bind(on_release=lambda _: climbCallback(EndingStates.MID))
        self.climb12.bind(on_release=lambda _: climbCallback(EndingStates.HIGH))
        
        climbLayout.add_widget(climbLabel)
        climbLayout.add_widget(self.climb0)
        climbLayout.add_widget(self.climb3)
        climbLayout.add_widget(self.climb6)
        climbLayout.add_widget(self.climb12)
        
        self.updateClimbLayout()
        leftSide.add_widget(climbLayout)
        
        # Helped layout
        helpedLayout = StackLayout(size_hint=(1, .5))
        
        helpedLabel = ColorLabel("Did the robot help another robot climb?", (1, .2), Colors.ORANGE)
        self.helped0 = ColorButton("Did not help", (1/3, .8), Colors.BLUE)
        self.helped6 = ColorButton("Helped climb for 6", (1/3, .8), Colors.FAIR_BLUE)
        self.helped12 = ColorButton("Helped climb for 12", (1/3, .8), Colors.LIGHT_BLUE)
        
        def helpedCallback(state):
            self.switcher.robot.helpedEndOn = state
            self.updateHelpedLayout()
        self.helped0.bind(on_release=lambda _: helpedCallback(EndingStates.NONE))
        self.helped6.bind(on_release=lambda _: helpedCallback(EndingStates.MID))
        self.helped12.bind(on_release=lambda _: helpedCallback(EndingStates.HIGH))
        
        helpedLayout.add_widget(helpedLabel)
        helpedLayout.add_widget(self.helped0)
        helpedLayout.add_widget(self.helped6)
        helpedLayout.add_widget(self.helped12)
        
        self.updateHelpedLayout()
        leftSide.add_widget(helpedLayout)
        
        self.notesInput = TextInput(text=self.switcher.robot.notes, size_hint=(1, .5), multiline=True)
        rightSide.add_widget(self.notesInput)
        
        # Rating layout
        ratingLayout = StackLayout(size_hint=(1, .3))
        
        ratingLabel = ColorLabel("Robot rating (1 is worst, 3 is best)", (1, .2), Colors.DEEP_BLUE)
        self.rating1 = ColorButton("1", (1/3, .8), Colors.BLUE)
        self.rating2 = ColorButton("2", (1/3, .8), Colors.FAIR_BLUE)
        self.rating3 = ColorButton("3", (1/3, .8), Colors.LIGHT_BLUE)
        
        def ratingCallback(rating):
            self.switcher.robot.rating = rating
            self.updateRatingLayout()
        self.rating1.bind(on_release=lambda _: ratingCallback(1))
        self.rating2.bind(on_release=lambda _: ratingCallback(2))
        self.rating3.bind(on_release=lambda _: ratingCallback(3))
        
        ratingLayout.add_widget(ratingLabel)
        ratingLayout.add_widget(self.rating1)
        ratingLayout.add_widget(self.rating2)
        ratingLayout.add_widget(self.rating3)
        
        self.updateRatingLayout()
        rightSide.add_widget(ratingLayout)
        
        backButton = ColorButton("Back", (.5, .2), Colors.LIGHT_RED)
        def backCallback(_):
            self.switcher.robot.notes = self.notesInput.text
            self.switcher.switch("scoring")
        backButton.bind(on_release=backCallback)
        rightSide.add_widget(backButton)
        
        endButton = ColorButton("End", (.5, .2), Colors.LIGHT_RED)
        def endCallback(_):
            self.switcher.robot.notes = self.notesInput.text
            self.switcher.robot.saveToLocalDB()
            self.switcher.switch("qr")
            #self.switcher.switch("login")
        endButton.bind(on_release=endCallback)
        rightSide.add_widget(endButton)
        
        self.clear_widgets()
        for widg in displist:
            self.add_widget(widg)
        
    def updateClimbLayout(self):
        self.climb0.background_color = Colors.DEEP_BLUE.asTupleWithAlpha()
        self.climb3.background_color = Colors.BLUE.asTupleWithAlpha()
        self.climb6.background_color = Colors.FAIR_BLUE.asTupleWithAlpha()
        self.climb12.background_color = Colors.LIGHT_BLUE.asTupleWithAlpha()
        
        if self.switcher.robot.endedOn == EndingStates.NONE:
            self.climb0.background_color = Colors.GREEN.asTupleWithAlpha()
        elif self.switcher.robot.endedOn == EndingStates.LOW:
            self.climb3.background_color = Colors.GREEN.asTupleWithAlpha()
        elif self.switcher.robot.endedOn == EndingStates.MID:
            self.climb6.background_color = Colors.GREEN.asTupleWithAlpha()
        elif self.switcher.robot.endedOn == EndingStates.HIGH:
            self.climb12.background_color = Colors.GREEN.asTupleWithAlpha()
        
    def updateHelpedLayout(self):
        self.helped0.background_color = Colors.BLUE.asTupleWithAlpha()
        self.helped6.background_color = Colors.FAIR_BLUE.asTupleWithAlpha()
        self.helped12.background_color = Colors.LIGHT_BLUE.asTupleWithAlpha()
        
        if self.switcher.robot.helpedEndOn == EndingStates.NONE:
            self.helped0.background_color = Colors.GREEN.asTupleWithAlpha()
        if self.switcher.robot.helpedEndOn == EndingStates.MID:
            self.helped6.background_color = Colors.GREEN.asTupleWithAlpha()
        if self.switcher.robot.helpedEndOn == EndingStates.HIGH:
            self.helped12.background_color = Colors.GREEN.asTupleWithAlpha()
    
    def updateRatingLayout(self):
        self.rating1.background_color = Colors.BLUE.asTupleWithAlpha()
        self.rating2.background_color = Colors.FAIR_BLUE.asTupleWithAlpha()
        self.rating3.background_color = Colors.LIGHT_BLUE.asTupleWithAlpha()
        
        if self.switcher.robot.rating == 1:
            self.rating1.background_color = Colors.GREEN.asTupleWithAlpha()
        if self.switcher.robot.rating == 2:
            self.rating2.background_color = Colors.GREEN.asTupleWithAlpha()
        if self.switcher.robot.rating == 3:
            self.rating3.background_color = Colors.GREEN.asTupleWithAlpha()
