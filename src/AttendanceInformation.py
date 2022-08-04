import sqlite3

class AttendanceInformation:
    def __init__(self):
        self.dbname = "Attendance.db"

    def getLectureName(self,lecture_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT lecture_name FROM attendanceInformation WHERE lecture_name=="{lecture_name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getAttendanceInformation(self,lecture_name, lecture_number):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT status FROM attendanceInformation WHERE lecture_name=="{lecture_name}" AND lecture_number=={lecture_number}')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getAllAttendanceInformation(self,lecture_name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT status FROM attendanceInformation WHERE lecture_name=="{lecture_name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result