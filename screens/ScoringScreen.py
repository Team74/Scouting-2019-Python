
from kivy.uix.stacklayout import StackLayout

from screens.ColorWidgets import ColorButton, ColorLabel, Colors
from screens.RotatingLayout import StartingLayout, HoldingLayout, PickupLayout

from robot.enums import Events

import time

class ScoringScreen(StackLayout):
    def __init__(self, switcher):
        super(ScoringScreen, self).__init__()
        self.switcher = switcher
        

    def display(self):
        displist = []
        
        # for alternating layout
        self.leftSide = StackLayout(size_hint=(.5, 1))
        
        self.rotatingLayout = StackLayout(size_hint=(1, .8))
        
        self.startingLayout = StartingLayout(self)
        self.holdingLayout = HoldingLayout(self)
        self.pickupLayout = PickupLayout(self)
        
        self.startingLayout.setNext(self.holdingLayout)
        self.holdingLayout.setNext(self.pickupLayout)
        self.pickupLayout.setNext(self.holdingLayout)
        
        self.rotatingLayout.add_widget(self.startingLayout)
        self.rotatingLayout.add_widget(self.holdingLayout)
        self.rotatingLayout.add_widget(self.pickupLayout)

        self.startingLayout.hide()
        self.holdingLayout.hide()
        self.pickupLayout.hide()

        robot = self.switcher.robot
        last = robot.getLast(robot.eventLog)
        if last != None:
            last = robot.eventLog[last]
        print("last = " + str(last))
        if last == None:
            self.startingLayout.show()
        elif last == Events.START:
            self.pickupLayout.show()
        elif last == Events.BALL or last == Events.DISC:
            self.holdingLayout.show()
        elif "scored" in last or "dropped" in last:
            self.pickupLayout.show()

        self.leftSide.add_widget(self.rotatingLayout)

        self.defenseButton = ColorButton("Defend (Robot crossed over middle line)", (.5, .2), Colors.BLUE)
        def defenseCallback(_):
            if not self.switcher.robot.isDefending:
                self.switcher.robot.defend()
            else:
                self.switcher.robot.undefend()
            self.updateUndoLayout()
            self.updateDefense()
        self.defenseButton.bind(on_press=defenseCallback)
        self.leftSide.add_widget(self.defenseButton)
        
        climbButton = ColorButton("We're in the endgame now", (.5, .2), Colors.LIGHT_RED)
        def climbCallback(_):
            self.switcher.switch("climb")
        climbButton.bind(on_press=climbCallback)
        self.leftSide.add_widget(climbButton)
        
        displist.append(self.leftSide)
        
        rightSide = StackLayout(size_hint=(.5, 1))
        
        self.scoreDisplay = StackLayout(size_hint=(1, .2))
        self.updateScoreDisplay()
        rightSide.add_widget(self.scoreDisplay)
        
        undoButton = ColorButton("undo", (1, .1), Colors.LIGHT_RED)
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
        undoButton.bind(on_press=undoCallback)
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