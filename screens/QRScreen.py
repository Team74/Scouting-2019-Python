import pyqrcode
import png
import sqlite3

from kivy.uix.image import Image
from kivy.uix.stacklayout import StackLayout

from screens.ColorWidgets import ColorButton, Colors

class QRScreen(StackLayout):
    def __init__(self, switcher):
        super(QRScreen, self).__init__()
        self.switcher = switcher
    
    def display(self):
        url = self.getURL()

        qr = pyqrcode.create(url)
        qr.png("qr", scale=8)

        self.clear_widgets()
        self.add_widget(Image(source="qr", size_hint=(1, .9)))

        exitButton = ColorButton("Exit", (1, .1), Colors.GREEN)
        exitButton.bind(on_release=lambda _: self.switcher.switch("login"))
        self.add_widget(exitButton)

    def getURL(self):
        db = sqlite3.connect("main.db")
        c = db.cursor()

        robot = self.switcher.robot

        roundNumber = robot.round
        c.execute("SELECT * FROM matchdata WHERE roundNumber>? AND roundNumber<=?", (roundNumber - 5, roundNumber))

        urlData = []
        for data in c.fetchall():
            print(data)
            teamNum = "%04d" % int(data[0]) if int(data[0]) <= 9999 else 9999
            roundNum = "%03d" % int(data[1]) if int(data[1]) <= 999 else 999
            ballsHigh = "%02d" % int(data[3]) if int(data[3]) <= 99 else 99
            ballsMid = "%02d" % int(data[4]) if int(data[4]) <= 99 else 99
            ballsLow = "%02d" % int(data[5]) if int(data[5]) <= 99 else 99
            discsHigh = "%02d" % int(data[7]) if int(data[7]) <= 99 else 99
            discsMid = "%02d" % int(data[8]) if int(data[8]) <= 99 else 99
            discsLow = "%02d" % int(data[9]) if int(data[9]) <= 99 else 99
            scouterRating = str(data[14])
            urlData.append(
                teamNum +
                roundNum +
                ballsHigh +
                ballsMid +
                ballsLow +
                discsHigh +
                discsMid +
                discsLow +
                scouterRating
            ) # TTTT RRR BH BM BL DH DM DL EE HH SS
            

        fullURL = "https://boost--the-basset-hound.repl.co/?pp" + "pp".join(urlData)

        db.close()

        return fullURL