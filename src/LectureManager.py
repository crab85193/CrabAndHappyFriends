import sqlite3

class LectureManager:
    def __init__(self):
        self.dbname = "Lecture.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        # cur.execute('CREATE TABLE lectureInformation(name STRING, time STRING, credits INTEGER, location STRING,professor_name STRING,rate_task INTEGER, rate_mid INTEGER, rate_final INTEGER,PRIMARY KEY(name,professor_name))')
        conn.commit()
        cur.close()
        conn.close()

    def addLectureInformation(self,name,time,credits,location,professor_name,rate_task,rate_mid,rate_final):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'INSERT INTO lectureInformation values("{name}","{time}",{credits},"{location}","{professor_name}",{rate_task},{rate_mid},{rate_final})')
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
