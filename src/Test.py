# from TaskInformation import TaskInformation
from Controller import Controller
from Model import Model

class Test:
    def __init__(self):
        self.controller = Controller()
        self.model = Model()

    def AttendanceTest(self):
        print("----- Attendance Test -----")
        self.controller.attendanceManager.addAttendanceInformation("講義名1","1","出席")
        self.controller.attendanceManager.addAttendanceInformation("講義名1","2","遅刻")
        self.controller.attendanceManager.addAttendanceInformation("講義名1","3","欠席")
        self.controller.attendanceManager.addAttendanceInformation("講義名2","1","遅刻")
        self.controller.attendanceManager.addAttendanceInformation("講義名2","2","欠席")
        self.controller.attendanceManager.addAttendanceInformation("講義名2","3","欠席")

        self.controller.attendanceManager.showData()

        print(self.model.attendanceInformation.getLectureName("講義名1"))
        print(self.model.attendanceInformation.getAttendanceInformation("講義名1","1"))
        print(self.model.attendanceInformation.getAttendanceInformation("講義名2","2"))
        print(self.model.attendanceInformation.getAllAttendanceInformation("講義名1"))

        self.controller.attendanceManager.deleteAllInformation()
        self.controller.attendanceManager.showData()

    def LectureTest(self):
        print("----- Lecture Test -----")
        self.controller.lectureManager.addLectureInformation("講義名1","8:30~10:00","2","ZoomLink","Mr.A","0.2","0.4","0.4")
        self.controller.lectureManager.addLectureInformation("講義名2","10:20~11:50","2","ZoomLink","Mr.B","0.4","0.2","0.4")

        self.controller.lectureManager.showData()

        print(self.model.lectureInformation.getName("講義名1"))
        print(self.model.lectureInformation.getTime("講義名1"))
        print(self.model.lectureInformation.getCredits("講義名2"))
        print(self.model.lectureInformation.getLocation("講義名2"))
        print(self.model.lectureInformation.getProfessorName("講義名1"))
        print(self.model.lectureInformation.getRateTask("講義名1"))
        print(self.model.lectureInformation.getRateMid("講義名2"))
        print(self.model.lectureInformation.getRateFinal("講義名2"))

        self.controller.lectureManager.deleteLectureInformation("name","講義名1")
        self.controller.lectureManager.showData()
        self.controller.lectureManager.deleteAllInformation()
        self.controller.lectureManager.showData()

    def ProfessorTest(self):
        print("----- Professor Test -----")
        self.controller.professorManager.addProfessorInformation("Mr.A","A@test.com")
        self.controller.professorManager.addProfessorInformation("Mr.B","B@test.com")

        self.controller.professorManager.showData()

        print(self.model.professorInformation.getName("Mr.A"))
        print(self.model.professorInformation.getContact("Mr.B"))

        self.controller.professorManager.deleteProfessorInformation("name","Mr.A")
        self.controller.professorManager.showData()
        self.controller.professorManager.deleteAllInformation()
        self.controller.lectureManager.showData()

    def TaskTest(self):
        print("----- Professor Test -----")
        self.controller.taskManager.addTaskInformation("講義名1","課題名1","2022/10/10","2022/10/08","★★")
        self.controller.taskManager.addTaskInformation("講義名1","課題名2","2022/10/15","2022/10/08","★")
        self.controller.taskManager.addTaskInformation("講義名2","課題名1","2022/10/8","2022/10/06","★★★")
        self.controller.taskManager.addTaskInformation("講義名2","課題名2","2022/10/29","2022/10/13","★★")

        self.controller.taskManager.showData()

        print(self.model.taskInformation.getLectureName("講義名1"))
        print(self.model.taskInformation.getAllTaskName("講義名1"))
        print(self.model.taskInformation.getTaskName("講義名2","課題名1"))
        print(self.model.taskInformation.getDeadlineDate("講義名2","課題名2"))
        print(self.model.taskInformation.getEffortDate("講義名1","課題名1"))
        print(self.model.taskInformation.getEffortDate("講義名1","課題名2"))

        self.controller.taskManager.deleteTaskInformation("task_name","課題1")
        self.controller.taskManager.showData()
        self.controller.taskManager.deleteAllInformation()
        self.controller.taskManager.showData()

    def main(self):
        # self.AttendanceTest()
        # self.LectureTest()
        # self.ProfessorTest()
        self.TaskTest()

if __name__ == '__main__':
    Test().main()