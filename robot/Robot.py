# pylint: disable=no-name-in-module
# pylint: disable=import-error

import time
import sqlite3

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
            Return a list of all of the integer fields in this class.
            """
        return [self.high, self.mid, self.low, self.dropped]

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

    def log(self, event, t=None):
        if not t:
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
        self.log(Events.START, getTime()-1) # we need to offset the time by one so that we don't have duplicate keys (overwritten start event)
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
        if self.getStart() == None: return # can't defend if we haven't started
            
        self.log(Events.DEFENSE)
        self.isDefending = True
    
    def undefend(self):
        self.log(Events.UNDEFENSE)
        self.isDefending = False

    def getCycles(self):
        """
            Return two lists of the time taken for the robot to score both game pieces.
            """
        times = list(self.eventLog.keys())
        class Cycles():
            def __init__(self):
                self.high = []
                self.mid = []
                self.low = []
                self.last = None
            
            def averages(self):
                self.high = round(sum(self.high) / len(self.high), 4) if len(self.high) > 0 else 0
                self.mid = round(sum(self.mid) / len(self.mid), 4) if len(self.mid) > 0 else 0
                self.low = round(sum(self.low) / len(self.low), 4) if len(self.low) > 0 else 0

        ballTimes = Cycles()
        discTimes = Cycles()
        
        times.sort()
        lastDefTime = None
        for time in times:
            event = self.eventLog[time]
            print("\n[getCycles] event: " + event + "\n[getCycles] time:  " + str(time))
            
            if   event == Events.BALL:
                ballTimes.last = time
            elif event == Events.DISC:
                discTimes.last = time
                
            elif event == Events.SCORE_BALL_LOW:
                ballTimes.low.append(time - ballTimes.last)
                ballTimes.last = None
            elif event == Events.SCORE_BALL_MID:
                ballTimes.mid.append(time - ballTimes.last)
                ballTimes.last = None
            elif event == Events.SCORE_BALL_HIGH:
                ballTimes.high.append(time - ballTimes.last)
                ballTimes.last = None
                
            elif event == Events.SCORE_DISC_LOW:
                discTimes.low.append(time - discTimes.last)
                discTimes.last = None
            elif event == Events.SCORE_DISC_MID:
                discTimes.mid.append(time - discTimes.last)
                discTimes.last = None
            elif event == Events.SCORE_DISC_HIGH:
                discTimes.high.append(time - discTimes.last)
                discTimes.last = None
            
            elif event == Events.DROP_BALL:
                ballTimes.last = None
            elif event == Events.DROP_DISC:
                discTimes.last = None
            
            elif event == Events.DEFENSE:
                lastDefTime = time
            elif event == Events.UNDEFENSE:
                if ballTimes.last != None:
                    ballTimes.last -= time - lastDefTime
                if discTimes.last != None:
                    discTimes.last -= time - lastDefTime
                lastDefTime = None
        ballTimes.averages()
        discTimes.averages()
        return ballTimes, discTimes

    def dumpData(self):
        """
            Returns all of the data stored within the robot that isn't 
            the team number or round number in the order it appears on
            the SQLite database.
            """
        return [self.scouter] + self.balls.dumpFields() + self.discs.dumpFields() + [self.endedOn, self.helpedEndOn, self.notes, self.rating]

    def saveToLocalDB(self):
        """
            Upload the robot's data to the local SQLite database.
            If data already exists for a team number + round number,
            overwrite that data.
            """
        db = sqlite3.connect("main.db")
        c = db.cursor()
        c.execute("""
            SELECT * FROM matchdata WHERE teamNumber=? AND roundNumber=?
        """, (self.number, self.round))
        if c.fetchone():
            db.execute("""
                UPDATE matchdata SET scouterName=?, 
                ballsHigh=?, ballsMid=?, ballsLow=?, ballsDropped=?,
                discsHigh=?, discsMid=?, discsLow=?, discsDropped=?,
                endedOn=?, helpedEndOn=?, notes=?, scouterRating=?
                WHERE teamNumber=? AND roundNumber=?
            """, self.dumpData() + [self.number, self.round])
        else:
            db.execute("""
                INSERT INTO matchdata VALUES
                    (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, [self.number, self.round] + self.dumpData())
            
        c.execute("""
            SELECT * FROM cycledata WHERE teamNumber=? AND roundNumber=?
        """, (self.number, self.round))
        
        
        bc, dc = self.getCycles()
        if c.fetchone():
            db.execute("""
               UPDATE cycledata SET
               ballLowAvg=?, ballMidAvg=?, ballHighAvg=?,
               discLowAvg=?, discMidAvg=?, discHighAvg=?
               WHERE teamNumber=? AND roundNumber=?
            """, [bc.low, bc.mid, bc.high, dc.low, dc.mid, dc.high, self.number, self.round])
        else:
            db.execute("""
                INSERT INTO cycledata VALUES
                    (?,?,?,?,?,?,?,?)
            """, [self.number, self.round, bc.low, bc.mid, bc.high, dc.low, dc.mid, dc.high])
            
        db.commit()
        db.close()
