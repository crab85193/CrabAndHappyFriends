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

    def calculate(self,lecture_name,late_task,late_mid,late_final):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT score,task_name FROM taskAssessmentInformation WHERE lecture_name=="{lecture_name}"')
        i = 0
        list = []
        result = 0
        task = 0
        counter = 0

        while 1:
            i = cur.fetchone()
            if type(i)==type(None): break
            list.append([i[0],i[1]])

        for j in list:
            print(j[1])
            print(j[0])
            if j[1]=='mid':
                result += j[0]*late_mid
            elif j[1]=='final':
                result += j[0]*late_final
            else:
                task += j[0]
                counter += 1
        result += (task/counter)*late_task

        cur.close()
        conn.close()

        return result


        # print(len(cur.fetchone()))
        # for i in range(len(cur.fetchall())):
        #     print(i)


