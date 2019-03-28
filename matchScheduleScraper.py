import bs4
import requests

import mysql.connector

eventURL = "2019miwmi"
soup = bs4.BeautifulSoup(requests.get("https://www.thebluealliance.com/event/%s" % eventURL).text, 'html.parser')

table = soup.find("table", class_="match-table")

matchSchedule = {}

for tr in table.find("tbody").find_all("tr", class_="visible-lg"):
    roundNum = int("".join([x for x in tr.find_all("td")[1].find("a").get_text() if x in "1234567890"]))
    matchSchedule[roundNum] = []
    for redTeamTd in tr.find_all("td", class_="red"):
        matchSchedule[roundNum].append(redTeamTd.find("a").get_text())
    for blueTeamTd in tr.find_all("td", class_="blue"):
        matchSchedule[roundNum].append(blueTeamTd.find("a").get_text())

db = mysql.connector.connect(
            connection_timeout=5,
            user="hostx75_scouting2019",
            passwd="chaos2019",
            host="secure209.inmotionhosting.com",
            database="hostx75_scouting2019"
        )
c = db.cursor()
for roundNum in matchSchedule:
    teams = matchSchedule[roundNum]
    c.execute("""
        DELETE FROM matchSchedule
    """)
    c.execute("""
        INSERT INTO matchSchedule VALUES
        (%s,%s,%s,%s,%s,%s,%s)
    """, [roundNum] + teams)
