import sqlite3

class TaskManager:
    def __init__(self):
        self.dbname = "Task.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        #cur.execute('CREATE TABLE taskInformation(lecture_name STRING, task_name STRING, deadline_date String, effort_date STRING,priority STRING, PRIMARY KEY(lecture_name,task_name))')
        conn.commit()
        cur.close()
        conn.close()

    def addTaskInformation(self,lecture_name,task_name,deadline_date,effort_date,priority):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'INSERT INTO taskInformation values("{lecture_name}","{task_name}","{deadline_date}","{effort_date}","{priority}")')
        conn.commit()
        cur.close()
        conn.close()

    def deleteTaskInformation(self,column,value):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM taskInformation where {column}=="{value}"')
        conn.commit()
        cur.close()
        conn.close()

    def deleteAllInformation(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM taskInformation')
        conn.commit()
        cur.close()
        conn.close()

    def showData(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute('SELECT * FROM taskInformation')
        print(cur.fetchall())
        cur.close()
        conn.close()