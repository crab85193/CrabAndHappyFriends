import sqlite3

class TaskInformation:
    def __init__(self):
        self.dbname = "Task.db"

    def getLectureName(self,lecture_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT lecture_name FROM taskInformation WHERE lecture_name=="{lecture_name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getAllTaskName(self,lecture_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT task_name FROM taskInformation WHERE lecture_name=="{lecture_name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result

    def getTaskName(self,lecture_name,task_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT task_name FROM taskInformation WHERE lecture_name=="{lecture_name}" AND task_name=="{task_name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result

    def getDeadlineDate(self,lecture_name,task_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT deadline_date FROM taskInformation WHERE lecture_name=="{lecture_name}" AND task_name=="{task_name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result

    def getEffortDate(self,lecture_name,task_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT deadline_date FROM taskInformation WHERE lecture_name=="{lecture_name}" AND task_name=="{task_name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getPriority(self,lecture_name,task_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT priority FROM taskInformation WHERE lecture_name=="{lecture_name}" AND task_name=="{task_name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]