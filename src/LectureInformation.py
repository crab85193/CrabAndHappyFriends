import sqlite3

class LectureInformation:
    def __init__(self):
        self.dbname = "Lecture.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        # cur.execute('CREATE TABLE lectureInformation(name STRING, time STRING, credits INTEGER, location STRING,professor_name STRING,rate_task INTEGER, rate_mid INTEGER, rate_final INTEGER,PRIMARY KEY(name,professor_name))')
        conn.commit()
        cur.close()
        conn.close()

    def getName(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT name FROM lectureInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getTime(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT time FROM lectureInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getCredits(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT credits FROM lectureInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getLocation(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT location FROM lectureInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getProfessorName(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT professor_name FROM lectureInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getProfessorContact(self,name):
        # conn = sqlite3.connect(self.dbname2)
        # cur = conn.cursor()
        # cur.execute(f'SELECT professorContact FROM professorInformation WHERE name=="{name}"')
        # self.result = cur.fetchall()
        # cur.close()
        # conn.close()
        # return self.result[0][0]
        pass

    def getRateTask(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT rate_task FROM lectureInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getRateMid(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT rate_mid FROM lectureInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getRateFinal(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT rate_final FROM lectureInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getAllInformation(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT time,name FROM lectureInformation')
        self.list = []
        self.result = []
        while 1:
            i = cur.fetchone()
            if type(i)==type(None): break
            self.list.append([i[0],i[1]])
        while 1:
            if len(self.list)>=8: break
            self.list.append([" "," "])

        cur.close()
        conn.close()

        for j in self.list:
            if j[0] == " ": self.result.append(j[0] + j[1])
            else: self.result.append(j[0] + " - " + j[1])
        return self.result