class LectureInformation:
    def __init__(self,name,time,credits,location,rate_task,rate_mid,rate_final):
        self.name = name
        self.time = time
        self.credits = credits
        self.location = location
        self.rate_task = rate_task
        self.rate_mid = rate_mid
        self.rate_final = rate_final

    def updateName(self,name):
        self.name = name

    def updateTime(self,time):
        self.time = time

    def updateLocation(self,location):
        self.location = location

    def updateProfessorName(self,name):
        pass

    def updateProfessorContact(self,contact):
        pass

    def updateRateTask(self,rate):
        self.rate_task = rate

    def updateRateMid(self,rate):
        self.rate_mid = rate

    def updateRateFinal(self,rate):
        self.rate_final = rate

    def getName(self):
        return self.name

    def getTime(self):
        return self.time

    def getCredits(self):
        return self.credits

    def getLocation(self):
        return self.location

    def getProfessorName(self):
        pass

    def getProfessorContact(self):
        pass

    def getRateTask(self):
        return self.rate_task

    def getRateMid(self):
        return self.rate_mid

    def getRateFinal(self):
        return self.rate_final