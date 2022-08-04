import sqlite3

class ProfessorManager:
    def __init__(self):
        self.dbname = "Professor.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        #cur.execute('CREATE TABLE professorInformation(name STRING PRIMARY KEY,contact String)')
        conn.commit()
        cur.close()
        conn.close()

    def addProfessorInformation(self,name,contact):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'INSERT INTO professorInformation values("{name}","{contact}")')
        conn.commit()
        cur.close()
        conn.close()

    def deleteProfessorInformation(self,column,value):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM professorInformation where {column}== "{value}"')
        conn.commit()
        cur.close()
        conn.close()

    def deleteAllInformation(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'DELETE FROM professorInformation')
        conn.commit()
        cur.close()
        conn.close()

    def showData(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute('SELECT * FROM professorInformation')
        print(cur.fetchall())
        cur.close()
        conn.close()