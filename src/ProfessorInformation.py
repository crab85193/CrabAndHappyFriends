import sqlite3

class ProfessorInformation:
    def __init__(self):
        self.dbname = "Professor.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        #cur.execute('CREATE TABLE professorInformation(name STRING PRIMARY KEY,contact String)')
        conn.commit()
        cur.close()
        conn.close()

    def getName(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT name FROM professorInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]

    def getContact(self,name):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT contact FROM professorInformation WHERE name=="{name}"')
        self.result = cur.fetchall()
        cur.close()
        conn.close()
        return self.result[0][0]