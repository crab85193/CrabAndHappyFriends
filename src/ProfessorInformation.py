class ProfessorInformation:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def updateName(self,name):
        self.name = name

    def updateContact(self,contact):
        self.contact = contact

    def getName(self):
        return self.name

    def getContact(self):
        return self.contact