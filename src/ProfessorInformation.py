class ProfessorInformation:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def setName(self,name):
        self.name = name

    def setContact(self,contact):
        self.contact = contact

    def getName(self):
        return self.name

    def getContact(self):
        return self.contact