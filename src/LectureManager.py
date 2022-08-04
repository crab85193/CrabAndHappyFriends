import sqlite3
import datetime
import re

class LectureManager:
    def __init__(self):
        self.dbname = "Lecture.db"
        self.dt_now = datetime.datetime.now()
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        # cur.execute('CREATE TABLE lectureInformation(name STRING, time STRING,weekday String, credits INTEGER, location STRING,professor_name STRING,rate_task INTEGER, rate_mid INTEGER, rate_final INTEGER,PRIMARY KEY(name,professor_name))')
        conn.commit()
        cur.close()
        conn.close()

    def addLectureInformation(self,name,time,weekday,credits,location,professor_name,rate_task,rate_mid,rate_final):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'INSERT INTO lectureInformation values("{name}","{time}","{weekday}",{credits},"{location}","{professor_name}",{rate_task},{rate_mid},{rate_final})')
        conn.commit()
        cur.close()
        conn.close()

    def deleteLectureInformation(self,column,value):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM lectureInformation where {column}== "{value}"')
        conn.commit()
        cur.close()
        conn.close()

    def deleteAllInformation(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM lectureInformation')
        conn.commit()
        cur.close()
        conn.close()

    def showData(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute('SELECT * FROM lectureInformation')
        print(cur.fetchall())
        cur.close()
        conn.close()

    def searchLectureOfTheHourNow(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        i = 0
        list = []
        cur.execute('SELECT name,time FROM lectureInformation')

        self.dt_now.strftime('%Y年%m月%d日 %H:%M:%S')

        while 1:
            i = cur.fetchone()
            if type(i)==type(None): break
            list.append([i[0],i[1]])

        for j in list:
            time = re.split("[:~]",j[1])
            # 基準となる時間
            base1 = datetime.time(int(time[0]), int(time[1]), 0)
            base2 = datetime.time(int(time[2]), int(time[3]), 0)

            # 現在時間
            dt_now = datetime.datetime.now()
            now = dt_now.time()
            if now >= base1 and now <= base2:
                return j[0]

        cur.close()
        conn.close()
        return "ないです"