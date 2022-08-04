# from LectureInformation import LectureInformation
from AttendanceInformation import AttendanceInformation
from LectureInformation import LectureInformation
from ProfessorInformation import ProfessorInformation
from TaskInformation import TaskInformation
from Calculator import Calculator

class Model:
    def __init__(self):
        self.attendanceInformation = AttendanceInformation()
        self.lectureInformation = LectureInformation()
        self.professorInformation = ProfessorInformation()
        self.taskInformation = TaskInformation()
        self.calculator = Calculator()



