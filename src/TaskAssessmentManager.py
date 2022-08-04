import sqlite3

class TaskAssessmentManager:
    def __init__(self):
        self.dbname = "TaskAssessment.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        #cur.execute('CREATE TABLE taskAssessmentInformation(lecture_name STRING, task_name STRING, score INTEGER)')
        conn.commit()
        cur.close()
        conn.close()

    def addScore(self,lecture_name,task_name,score):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'INSERT INTO taskAssessmentInformation values("{lecture_name}","{task_name}","{score}")')
        conn.commit()
        cur.close()
        conn.close()

    def deleteTaskAssessmentInformation(self,column,value):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM taskAssessmentInformation where {column}=="{value}"')
        conn.commit()
        cur.close()
        conn.close()

    def deleteAllInformation(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM taskAssessmentInformation')
        conn.commit()
        cur.close()
        conn.close()

    def showData(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute('SELECT * FROM taskAssessmentInformation')
        print(cur.fetchall())
        cur.close()
        conn.close()