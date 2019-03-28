from kivy.uix.stacklayout import StackLayout

from screens.ColorWidgets import ColorButton, ColorLabel, Colors

from robot.enums import Events

class RotatingLayout(StackLayout):
    def __init__(self):
        super(RotatingLayout, self).__init__()
    
    def setNext(self, nextLayout):
        self.next = nextLayout
    
    def displayNext(self):
        self.hide()
        self.next.show()
    
    def show(self):
        self.size_hint = (1, 1) # y=1.0275 to fix visual glitch w kivy # fixed itself on tablets?
        
    def hide(self):
        self.size_hint = (1, 0)
        self.pos = (10, 10)

class StartingLayout(RotatingLayout):
    """
        Displayed as the robot has not started the match yet.
        """
    def __init__(self, switcher):
        super(StartingLayout, self).__init__()
        self.parentLayout = switcher
        self.robot = switcher.switcher.robot
        self.build()
        
    def build(self):
        startBallButton = ColorButton("Started with ball (starts game timer)", (1, 1/3), Colors.ORANGE)
        def ballCallback(_):
            if self.robot.balls.has or self.robot.discs.has:
                return
            self.robot.start(Events.BALL)
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        startBallButton.bind(on_press=ballCallback)
        self.add_widget(startBallButton)
        
        startDiscButton = ColorButton("Started with disc (starts game timer)", (1, 1/3), Colors.YELLOW)
        def discCallback(_):
            if self.robot.balls.has or self.robot.discs.has: # check if buttons are pressed simultaneously, essentially
                return
            self.robot.start(Events.DISC)
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        startDiscButton.bind(on_press=discCallback)
        self.add_widget(startDiscButton)

        startNoneButton = ColorButton("Started with nothing (starts game timer)", (1, 1/3), Colors.LIGHT_RED)
        def noneCallback(_):
            if self.robot.balls.has or self.robot.discs.has:
                return
            self.robot.start(None)
            self.parentLayout.updateUndoLayout()
            self.displayNext()
            self.next.displayNext()
        startNoneButton.bind(on_press=noneCallback)
        self.add_widget(startNoneButton)

class HoldingLayout(RotatingLayout):
    """
        Displayed as the robot is in control of a game piece.
        """
    def __init__(self, switcher):
        super(HoldingLayout, self).__init__()
        self.parentLayout = switcher
        self.robot = switcher.switcher.robot
        self.build()
    
    def build(self):
        scoredHighButton = ColorButton("Scored high", (1, .25), Colors.LIGHT_BLUE)
        def highCallback(_):
            if self.robot.isDefending:
                return
            self.robot.scoreCurrentHigh()
            self.parentLayout.updateScoreDisplay()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        scoredHighButton.bind(on_press=highCallback)
        self.add_widget(scoredHighButton)
        
        scoredMidButton = ColorButton("Scored mid", (1, .25), Colors.FAIR_BLUE)
        def midCallback(_):
            if self.robot.isDefending:
                return
            self.robot.scoreCurrentMid()
            self.parentLayout.updateScoreDisplay()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        scoredMidButton.bind(on_press=midCallback)
        self.add_widget(scoredMidButton)
        
        scoredLowButton = ColorButton("Scored low", (1, .25), Colors.BLUE)
        def lowCallback(_):
            if self.robot.isDefending:
                return
            self.robot.scoreCurrentLow()
            self.parentLayout.updateScoreDisplay()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        scoredLowButton.bind(on_press=lowCallback)
        self.add_widget(scoredLowButton)
        
        droppedButton = ColorButton("Dropped", (1, .25), Colors.DEEP_BLUE)
        def droppedCallback(_):
            self.robot.dropCurrent()
            self.parentLayout.updateScoreDisplay()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        droppedButton.bind(on_press=droppedCallback)
        self.add_widget(droppedButton)


class PickupLayout(RotatingLayout):
    """
        Displayed as the robot is not in control of any game pieces.
        """
    def __init__(self, switcher):
        super(PickupLayout, self).__init__()
        self.parentLayout = switcher
        self.robot = switcher.switcher.robot
        self.build()
        
    def build(self):
        ballButton = ColorButton("Picked up ball", (1, .5), Colors.ORANGE)
        def ballCallback(_):
            if self.robot.isDefending or self.robot.balls.has or self.robot.discs.has:
                return
            self.robot.pickUpBall()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        ballButton.bind(on_press=ballCallback)
        self.add_widget(ballButton)
        
        discButton = ColorButton("Picked up disc", (1, .5), Colors.YELLOW)
        def discCallback(_):
            if self.robot.isDefending or self.robot.balls.has or self.robot.discs.has:
                return
            self.robot.pickUpDisc()
            self.parentLayout.updateUndoLayout()
            self.displayNext()
        discButton.bind(on_press=discCallback)
        self.add_widget(discButton)
