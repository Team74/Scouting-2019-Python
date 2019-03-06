# pylint: disable=no-name-in-module
# pylint: disable=import-error

import time

from robot.enums import EndingStates
from robot.enums import Events

def getTime():
    return int(round(time.time() * 1000))
    
class Scoring():
    """
        Helper for scoring. Stores how many game pieces were scored in each level.
        """
    def __init__(self):
        """ How many pieces were scored in the transport or the low rocket ship level. """
        self.low = 0
        """ How many pieces were scored in the middle rocket ship level. """
        self.mid = 0
        """ How many pieces were scored in the high rocket ship level. """
        self.high = 0
        """ How many pieces were dropped. """
        self.dropped = 0

        """ Whether or not a piece is currently picked up. """
        self.has = False
    
    def dumpFields(self):
        """
            Return a list of all of the integer fields in this class in the order they are defined above.
            """
        return [self.low, self.mid, self.high, self.dropped]

class Robot():
    """
        Where all of the data on a robot is stored.
        """
    def __init__(self, number, roundNum, scouter):
        """ The team number of the robot. """
        self.number = number
        """ The round number the robot is participating in. """
        self.round = roundNum
        """ The person scouting the robot. """
        self.scouter = scouter
        
        """ A series of millisecond timestamps mapped to events (ints). """
        self.eventLog = {}
        
        """ Scoring information for how many balls the robot has scored / dropped. """
        self.balls = Scoring()
        """ Scoring information for how many discs the robot has scored / dropped. """
        self.discs = Scoring()
        
        """ Whether or not the robot started on the 6 point platform to begin the match. """
        self.gotStartingBonus = False
        """ Whether or not the robot is over the defending line. """
        self.isDefending = False
        """ Which platform the robot ended on. """
        self.endedOn = EndingStates.NONE
        """ Which platform the robot helped another robot get to. """
        self.helpedEndOn = EndingStates.NONE
        
        """ How the scouter ranked the robot at the end of the round. """
        self.rating = 0
        """ General notes that the scouter takes on the robot. """
        self.notes = ""

    def log(self, event):
        t = getTime()
        print("logging `" + event + "` at time " + str(t))
        self.eventLog[t] = event
    
    def unlog(self):
        """
            Pop the last event that happened off of the eventLog and return its event.
            If the last event to happen was the starting event or the eventLog is empty, return None.
            """
        allKeys = self.eventLog.keys()
        if len(allKeys) == 0: return None
        lastTime = max(allKeys)
        if (self.eventLog[lastTime] == Events.START): return None
        lastEvent = self.eventLog.pop(lastTime)
        print("unlogging `" + lastEvent + "` at time " + str(lastTime))
        
        if lastEvent == Events.BALL:
            self.balls.has = False
        elif lastEvent == Events.DISC:
            self.discs.has = False
        elif lastEvent == Events.SCORE_BALL_HIGH:
            self.balls.high -= 1
            self.balls.has = True
        elif lastEvent == Events.SCORE_BALL_MID:
            self.balls.mid -= 1
            self.balls.has = True
        elif lastEvent == Events.SCORE_BALL_LOW:
            self.balls.low -= 1
            self.balls.has = True
        elif lastEvent == Events.DROP_BALL:
            self.balls.dropped -= 1
            self.balls.has = True
        elif lastEvent == Events.SCORE_DISC_HIGH:
            self.discs.high -= 1
            self.discs.has = True
        elif lastEvent == Events.SCORE_DISC_MID:
            self.discs.mid -= 1
            self.discs.has = True
        elif lastEvent == Events.SCORE_DISC_LOW:
            self.discs.low -= 1
            self.discs.has = True
        elif lastEvent == Events.DROP_DISC:
            self.discs.dropped -= 1
            self.discs.has = True
        elif lastEvent == Events.DEFENSE:
            self.isDefending = False
        elif lastEvent == Events.UNDEFENSE:
            self.isDefending = True
        
        return lastEvent

    def start(self, startingPiece):
        """
            Logs a start event and logs an event based on what piece the robot started with.
            """
        self.log(Events.START)
        time.sleep(.001)
        if startingPiece == Events.BALL:
            print("Robot is starting with Events.BALL")
            self.pickUpBall()
        if startingPiece == Events.DISC:
            print("Robot is starting with Events.DISC")
            self.pickUpDisc()
    
    def getStart(self):
        """
            Returns the timestamp that the start event happened.
            """
        for time in self.eventLog.keys():
            if self.eventLog[time] == Events.START:
                return time
    
    def scoreCurrentLow(self):
        if self.balls.has:
            self.log(Events.SCORE_BALL_LOW)
            self.balls.low += 1
            self.balls.has = False
        elif self.discs.has:
            self.log(Events.SCORE_DISC_LOW)
            self.discs.low += 1
            self.discs.has = False
    
    def scoreCurrentMid(self):
        if self.balls.has:
            self.log(Events.SCORE_BALL_MID)
            self.balls.mid += 1
            self.balls.has = False
        elif self.discs.has:
            self.log(Events.SCORE_DISC_MID)
            self.discs.mid += 1
            self.discs.has = False
    
    def scoreCurrentHigh(self):
        if self.balls.has:
            self.log(Events.SCORE_BALL_HIGH)
            self.balls.high += 1
            self.balls.has = False
        elif self.discs.has:
            self.log(Events.SCORE_DISC_HIGH)
            self.discs.high += 1
            self.discs.has = False
    
    def dropCurrent(self):
        if self.balls.has:
            self.log(Events.DROP_BALL)
            self.balls.has = False
        elif self.discs.has:
            self.log(Events.DROP_DISC)
            self.discs.has = False
        
    def pickUpBall(self):
        self.log(Events.BALL)
        self.balls.has = True
    
    def pickUpDisc(self):
        self.log(Events.DISC)
        self.discs.has = True

    def defend(self):
        if self.getStart() == None: return
            
        self.log(Events.DEFENSE)
        self.isDefending = True
    
    def undefend(self):
        self.log(Events.UNDEFENSE)
        self.isDefending = False
