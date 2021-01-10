from bs4 import BeautifulSoup
import re
import mysql.connector
from urllib.request import urlopen

url = "https://www.battle-report.com/2019/12/21/warhammer-40k-itc-champions-missions-necrons-vs-ultramarines/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
#boolean needed to check if a yutube viideo is present
#battle reports with video never contain results, only army list
result = soup.find("div", {"class": "entry-content"})
text = result.get_text()

#remove unnecessary text
text = re.sub(r"\. .*\n", "", text)
text = re.sub(re.compile(r"^.*https://www.battle-report.com/", re.DOTALL), "", text)
text = re.sub(r"\[.*", "", text)

#1st player units
armyRaw = re.search(r"\+ HQ (.*?)Total", text, re.DOTALL).group(0)
armyRaw = re.sub(r"\+.*\n", "", armyRaw)
armyRaw = re.sub(r"Detachment CP .*\n", "", armyRaw)
armyRaw = re.sub(r"\*.*\n", "", armyRaw)
#print(armyRaw)

#2nd player units
army2Raw = re.sub(re.compile(r"^.*Army List", re.DOTALL), "", text)
army2Raw = re.search(r"\+ HQ (.*?)Total", army2Raw, re.DOTALL).group(1)
army2Raw = re.sub(r"\+.*\n", "", army2Raw)
army2Raw = re.sub(r"Detachment CP .*\n", "", army2Raw)
army2Raw = re.sub(r"\*.*\n", "", army2Raw)
#print(army2Raw)

#Match Result
resultRaw = re.sub(re.compile(r"^.*Final Score", re.DOTALL), "", text)
def getNumbers(str):
    array = re.findall(r"[0-9]+", str)
    return array


points = getNumbers(resultRaw)
p1result = points[0]
p2result = points[1]

armyList=armyRaw.splitlines()
armyList.pop()
while len(armyList)<=25:
    armyList.append(None)

army2List=army2Raw.splitlines()
army2List.pop()
while len(army2List)<=25:
    army2List.append(None)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="projectdb"
)
mycursor = mydb.cursor()

sql = "BEGIN;" \
      "INSERT INTO result (p1points, p2points)" \
      "VALUES( %s, %s); " \
      "INSERT INTO army1 (resultID, unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8, unit9, unit10, " \
      "unit11, unit12, unit13, unit14, unit15, unit16, unit17, unit18, unit19, unit20, unit21, unit22, " \
      "unit23, unit24, unit25)" \
      "Values( LAST_INSERT_ID(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
      "%s, %s, %s, %s);" \
      "INSERT INTO army2 (resultID, unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8, unit9, unit10, " \
      "unit11, unit12, unit13, unit14, unit15, unit16, unit17, unit18, unit19, unit20, unit21, unit22, " \
      "unit23, unit24, unit25)" \
      "Values( LAST_INSERT_ID(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
      "%s, %s, %s, %s);" \
      "COMMIT;"

val= (p1result, p2result,
      armyList[0], armyList[1], armyList[2], armyList[3], armyList[4],
      armyList[5], armyList[6], armyList[7], armyList[8], armyList[9],
      armyList[10], armyList[11], armyList[12], armyList[13], armyList[14],
      armyList[15], armyList[16], armyList[17], armyList[18], armyList[19],
      armyList[20], armyList[21], armyList[22], armyList[23], armyList[24],
      army2List[0], army2List[1], army2List[2], army2List[3], army2List[4],
      army2List[5], army2List[6], army2List[7], army2List[8], army2List[9],
      army2List[10], army2List[11], army2List[12], army2List[13], army2List[14],
      army2List[15], army2List[16], army2List[17], army2List[18], army2List[19],
      army2List[20], army2List[21], army2List[22], army2List[23], army2List[24])

mycursor.execute(sql, val, multi=True)

mydb.commit()
print (army2List[3])
print("game recorded")
