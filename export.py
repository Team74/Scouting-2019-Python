# 204.8.232.45 is ip for old MySQL db

# secure209.inmotionhosting.com
# hostx75_scouting2019
# chaos2019

import mysql.connector
import sqlite3
import sys

def export():
    print(sys.version)
    try:
        db = mysql.connector.connect(
            connection_timeout=5,
            user="hostx75_scouting2019",
            passwd="chaos2019",
            host="secure209.inmotionhosting.com",
            database="hostx75_scouting2019"
        )
    except mysql.connector.errors.InterfaceError as e:
        print(e.msg)
        return "Failed to upload - timed out or IP was incorrect"
    except mysql.connector.errors.OperationalError as e:
        print(str(e))
        return "youre trying to export from haworth you dumbass"
    c = db.cursor()
    
    ldb = sqlite3.connect("main.db")
    lc = ldb.cursor()
    
    lc.execute("SELECT * FROM matchdata")
    for row in lc.fetchall():
        c.execute("""
            SELECT * FROM matchdata WHERE teamNumber=%s AND roundNumber=%s
        """, [row[0], row[1]])
        print("looking for teamNumber %s and roundNumber %s" % (row[0], row[1]))
        if c.fetchone():
            print("Found a match, UPDATEing")
            c.execute("""
                UPDATE matchdata SET
                scouterName=%s,
                ballsHigh=%s, ballsMid=%s, ballsLow=%s, ballsDropped=%s,
                discsHigh=%s, discsMid=%s, discsLow=%s, discsDropped=%s,
                endedOn=%s, helpedEndOn=%s, notes=%s, scouterRating=%s
                WHERE teamNumber=%s AND roundNumber=%s
            """, row[2:] + row[:2])
        else:
            print("Did not find a match, INSERTing")
            c.execute("""
                INSERT INTO matchdata VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, row)
    
    lc.execute("SELECT * FROM cycledata")
    for row in lc.fetchall():
        c.execute("""
            SELECT * FROM cycledata WHERE teamNumber=%s AND roundNumber=%s
        """, row[0], row[1])
        print("looking for teamNumber %s and roundNumber %s" % (row[0], row[1]))

        if c.fetchone():
            print("Found a match, UPDATEing")
            c.execute("""
                UPDATE cycledata SET
                ballLowAvg=%s, ballMidAvg=%s, ballHighAvg=%s,
                discLowAvg=%s, discMidAvg=%s, discHighAvg=%s
                WHERE teamNumber=%s AND roundNumber=%s
            """, row[2:] + row[:2])
        else:
            print("Did not find a match, INSERTing")
            c.execute("""
                INSERT INTO cycledata SET
                (%s,%s,%s,%s,%s,%s,%s,%s)
            """)

    db.commit()
    
    ldb.close()
    db.close()
    return "Successfully uploaded data"
