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

    def addAttendanceInformation(self,lecture_name,status):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        lecture_number = None
        cur.execute(f'SELECT MAX(lecture_number) FROM attendanceInformation WHERE lecture_name=="{lecture_name}"')
        i = cur.fetchone()
        if type(i[0]) == type(None):
            lecture_number = 1
        else:
            lecture_number = int(i[0]) + 1
            print(lecture_number)

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