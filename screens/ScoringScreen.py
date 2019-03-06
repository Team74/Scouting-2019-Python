
from kivy.uix.stacklayout import StackLayout

from screens.ColorWidgets import ColorButton, ColorLabel, Colors

from robot.enums import Events

import time

class ScoringScreen(StackLayout):
    def __init__(self, switcher):
        super(ScoringScreen, self).__init__()
        self.switcher = switcher
        

    def display(self):
        displist = []
        
        # for alternating layout
        leftSide = StackLayout(size_hint=(.5, 1))
        
        rotatingLayout = StackLayout(size_hint=(1, .8))
        
        self.startingLayout = StartingLayout(self)
        self.holdingLayout = HoldingLayout(self)
        self.pickupLayout = PickupLayout(self)
        
        self.startingLayout.setNext(self.holdingLayout)
        self.holdingLayout.setNext(self.pickupLayout)
        self.pickupLayout.setNext(self.holdingLayout)
        
        rotatingLayout.add_widget(self.startingLayout)
        rotatingLayout.add_widget(self.holdingLayout)
        rotatingLayout.add_widget(self.pickupLayout)
        leftSide.add_widget(rotatingLayout)
        
        self.defenseButton = ColorButton("Defend (Robot crossed over middle line)", (.5, .2), Colors.LIGHT_RED)
        def defenseCallback(_):
            if not self.switcher.robot.isDefending:
                self.switcher.robot.defend()
            else:
                self.switcher.robot.undefend()
            self.updateUndoLayout()
            self.updateDefense()
        self.defenseButton.bind(on_release=defenseCallback)
        leftSide.add_widget(self.defenseButton)
        
        climbButton = ColorButton("Climb", (.5, .2), Colors.LIGHT_RED)
        def climbCallback(_):
            self.switcher.switch("climb")
        climbButton.bind(on_release=climbCallback)
        leftSide.add_widget(climbButton)
        
        displist.append(leftSide)
        
        rightSide = StackLayout(size_hint=(.5, 1))
        
        self.scoreDisplay = StackLayout(size_hint=(1, .2))
        self.updateScoreDisplay()
        rightSide.add_widget(self.scoreDisplay)
        
        undoButton = ColorButton("undo", (1, .1,), Colors.LIGHT_RED)
        def undoCallback(_):
            event = self.switcher.robot.unlog()
            self.updateUndoLayout()
            self.updateScoreDisplay()
            if event == Events.BALL or event == Events.DISC:
                self.holdingLayout.displayNext()
            elif event != None and event != Events.DEFENSE and event != Events.UNDEFENSE:
                self.pickupLayout.displayNext()
            else:
                self.updateDefense()
        undoButton.bind(on_release=undoCallback)
        rightSide.add_widget(undoButton)
        
        self.undoLayout = StackLayout(size_hint=(1, .7))
        self.undoLayout.alternate = False
        self.updateUndoLayout()
        rightSide.add_widget(self.undoLayout)
        
        displist.append(rightSide)
        
        self.clear_widgets()
        for widg in displist:
            self.add_widget(widg)
    
    def updateDefense(self):
        if not self.switcher.robot.isDefending:
            self.defenseButton.text = "Defend (Robot crossed over middle line)"
        else:
            self.defenseButton.text = "Stop defending (Robot crossed back over middle line)"
        
    def updateUndoLayout(self):
        self.undoLayout.clear_widgets()
        
        log = self.switcher.robot.eventLog
        start = self.switcher.robot.getStart()
        if start == None:
            return
        allTimes = list(log.keys())
        allTimes.reverse()
        for time in allTimes:
            event = log[time]
            
            text = event + " at " + str(time - start)
            
            alternatingColor = Colors.LIGHT_MAGENTA
            if self.undoLayout.alternate:
                alternatingColor = alternatingColor.muteNew()
            self.undoLayout.alternate = not self.undoLayout.alternate
            
            self.undoLayout.add_widget(ColorLabel(text, (1, .05), alternatingColor))
    
    def updateScoreDisplay(self):
        self.scoreDisplay.clear_widgets()
        
        robot = self.switcher.robot
                
        robotTeam = ColorLabel("Team: " + str(robot.number), (.5, .6), Colors.GREEN)
        robotRound = ColorLabel("Round: " + str(robot.round), (.5, .6), Colors.GREEN)
        robotScouter = ColorLabel("Scouter: " + str(robot.scouter), (1, .4), Colors.GREEN)
        
        self.scoreDisplay.add_widget(robotTeam)
        self.scoreDisplay.add_widget(robotRound)
        self.scoreDisplay.add_widget(robotScouter)

class RotatingLayout(StackLayout):
    def __init__(self):
        super(RotatingLayout, self).__init__()
    
    def setNext(self, nextLayout):
        self.next = nextLayout
    
    def displayNext(self):
        self.hide()
        self.next.show()
    
    def show(self):
        self.size_hint = (1, 1)
        
    def hide(self):
        self.size_hint = (0, 0)

class StartingLayout(RotatingLayout):
    """
        Displayed as the robot has not started the match yet.
        """
    def __init__(self, switcher):
        super(StartingLayout, self).__init__()
        self.parentLayout = switcher
        self.build()
        
    def build(self):
        startBallButton = ColorButton("Started with ball", (1, .5), Colors.ORANGE)
        def ballCallback(_):
            self.parentLayout.switcher.robot.start(Events.BALL)
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        startBallButton.bind(on_release=ballCallback)
        self.add_widget(startBallButton)
        
        startDiscButton = ColorButton("Started with disc", (1, .5), Colors.YELLOW)
        def discCallback(_):
            self.parentLayout.switcher.robot.start(Events.DISC)
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        startDiscButton.bind(on_release=discCallback)
        self.add_widget(startDiscButton)

class HoldingLayout(RotatingLayout):
    """
        Displayed as the robot is in control of a game piece.
        """
    def __init__(self, switcher):
        super(HoldingLayout, self).__init__()
        self.parentLayout = switcher
        self.build()
    
    def build(self):
        scoredHighButton = ColorButton("Scored high", (1, .25), Colors.LIGHT_BLUE)
        def highCallback(_):
            self.parentLayout.switcher.robot.scoreCurrentHigh()
            self.parentLayout.updateScoreDisplay()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        scoredHighButton.bind(on_release=highCallback)
        self.add_widget(scoredHighButton)
        
        scoredMidButton = ColorButton("Scored mid", (1, .25), Colors.FAIR_BLUE)
        def midCallback(_):
            self.parentLayout.switcher.robot.scoreCurrentMid()
            self.parentLayout.updateScoreDisplay()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        scoredMidButton.bind(on_release=midCallback)
        self.add_widget(scoredMidButton)
        
        scoredLowButton = ColorButton("Scored low", (1, .25), Colors.BLUE)
        def lowCallback(_):
            self.parentLayout.switcher.robot.scoreCurrentLow()
            self.parentLayout.updateScoreDisplay()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        scoredLowButton.bind(on_release=lowCallback)
        self.add_widget(scoredLowButton)
        
        droppedButton = ColorButton("Dropped", (1, .25), Colors.DEEP_BLUE)
        def droppedCallback(_):
            self.parentLayout.switcher.robot.dropCurrent()
            self.parentLayout.updateScoreDisplay()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        droppedButton.bind(on_release=droppedCallback)
        self.add_widget(droppedButton)

class PickupLayout(RotatingLayout):
    """
        Displayed as the robot has not started the match yet.
        """
    def __init__(self, switcher):
        super(PickupLayout, self).__init__()
        self.parentLayout = switcher
        self.build()
        
    def build(self):
        ballButton = ColorButton("Picked up ball", (1, .5), Colors.ORANGE)
        def ballCallback(_):
            self.parentLayout.switcher.robot.pickUpBall()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        ballButton.bind(on_release=ballCallback)
        self.add_widget(ballButton)
        
        discButton = ColorButton("Picked up disc", (1, .5), Colors.YELLOW)
        def discCallback(_):
            self.parentLayout.switcher.robot.pickUpDisc()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        discButton.bind(on_release=discCallback)
        self.add_widget(discButton)
