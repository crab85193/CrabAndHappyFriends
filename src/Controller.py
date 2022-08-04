from Model import Model

from LectureManager import LectureManager
from TaskManager import TaskManager
from AttendanceManager import AttendanceManager
from ProfessorManager import ProfessorManager

class Controller:
    def __init__(self):
        self.model = Model()
        self.lectureManager = LectureManager()
        self.taskManager = TaskManager()
        self.attendanceManager = AttendanceManager()
        self.professorManager = ProfessorManager()

    def setLectureInformation(self,name,time,credits,location,professor_name,rate_task,rate_mid,rate_final):
        self.lectureManager.addLectureInformation(name,time,credits,location,professor_name,rate_task,rate_mid,rate_final)

    def setTaskInformation(self,lecture_name,task_name,deadline_date,effort_date,priority):
        self.taskManager.addTaskInformation(lecture_name,task_name,deadline_date,effort_date,priority)

    def setAttendanceInformation(self,lecture_name,lecture_number,status):
        self.attendanceManager.addAttendanceInformation(lecture_name,lecture_number,status)

    def setProfessorInformation(self,name,contact):
        self.professorManager.addProfessorInformation(name,contact)

    def on_press(self):
       self.text = "ボタンを押した"