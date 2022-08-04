import sqlite3

class Calculator:
    def __init__(self):
        self.dbname = "TaskAssessment.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        #cur.execute('CREATE TABLE taskAssessmentInformation(lecture_name STRING, task_name STRING, score INTEGER)')
        conn.commit()
        cur.close()
        conn.close()

        self.rate_task = 0
        self.rate_mid = 0
        self.rate_final = 0
        self.task_score_list = list()
        self.task_score = 0
        self.mid_score = 0
        self.final_score = 0

    def setParameter(self,rate_task,rate_mid,rate_final):
        self.rate_task = rate_task
        self.rate_mid = rate_mid
        self.rate_final = rate_final

    def addScore(self,lecture_name,task_name,score,type):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'INSERT INTO taskAssessmentInformation values("{lecture_name}","{task_name}","{score}")')
        conn.commit()
        cur.close()
        conn.close()
        # if type=='task':
        #     self.task_score_list.append(score)
        # elif type=='mid':
        #     self.mid_score = score
        # elif type=='final':
        #     self.final_score = score
        # else:
        #     pass

    def calculate(self,lecture_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT score FROM taskAssessmentInformation WHERE lecture_name=="{lecture_name}"')
        print(cur.fetchall()[1][0])
        print(len(cur.fetchall()))
        for i in range(len(cur.fetchall())):
            print(i)
        cur.close()
        conn.close()
        # for i in self.task_score_list:
        #     self.task_score += i

        # self.result = self.task_score * self.rate_task + self.mid_score * self.rate_mid + self.final_score * self.rate_final

        # return self.result

    def deleteTaskAssessmentInformation(self,column,value):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM taskAssessmentInformation where {column}=="{value}"')
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