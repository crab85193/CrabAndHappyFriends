import sqlite3

class AttendanceManager:
    def __init__(self):
        self.dbname = "Attendance.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        # cur.execute('CREATE TABLE attendanceInformation(lecture_name STRING, lecture_number INTEGER, status STRING)')
        conn.commit()
        cur.close()
        conn.close()

    def addAttendanceInformation(self,lecture_name,lecture_number,status):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'INSERT INTO attendanceInformation values("{lecture_name}","{lecture_number}","{status}")')
        conn.commit()
        cur.close()
        conn.close()

    def deleteAttendanceInformation(self,column,value):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM attendanceInformation where {column}=="{value}"')
        conn.commit()
        cur.close()
        conn.close()

    def deleteAllInformation(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM attendanceInformation')
        conn.commit()
        cur.close()
        conn.close()

    def showData(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute('SELECT * FROM attendanceInformation')
        print(cur.fetchall())
        cur.close()
        conn.close()