from calendar import weekday
from ctypes.wintypes import SMALL_RECT
import datetime
import calendar
from logging import getLevelName
from modulefinder import Module
from select import select
from tokenize import String

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import ObjectProperty, BooleanProperty

from kivy.lang import Builder

from Model import Model
from Controller import Controller

import datetime
import sqlite3
import re

####日本語対応用コード
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分
resource_add_path('/System/Library/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')  # 追加分
####日本語対応ここまで

#ウィンドウサイズの定義
Config.set('graphics', 'width', 1200)
Config.set('graphics', 'height', 800)
Config.set('graphics', 'resizable', 0)

model = Model()
controller = Controller()

#popupクラス達
sm=ScreenManager()
class PopupMenu1(BoxLayout):
    popup_close = ObjectProperty(None)

class PopupMenu2(BoxLayout):
    popup_close = ObjectProperty(None)

class PopupMenu3(BoxLayout):
    popup_close = ObjectProperty(None)


class PopupTest(Screen):
    def popup_open(self):
        content = PopupMenu1(popup_close=self.popup_close)
        self.popup = Popup(title='課題追加', content=content, size_hint=(0.5, 0.5), auto_dismiss=True)
        self.popup.open()

class PopupTest(Screen):
    def popup_open(self):
        content = PopupMenu2(popup_close=self.popup_close)
        self.popup = Popup(title='履修講義追加', content=content, size_hint=(0.5, 0.5), auto_dismiss=True)
        self.popup.open()

class PopupTest(Screen):
    def popup_open(self):
        content = PopupMenu3(popup_close=self.popup_close)
        self.popup = Popup(title='履修講義名', content=content, size_hint=(0.5, 0.5), auto_dismiss=True)
        self.popup.open()


class PopupApp(App):
    def build(self):
        sm.add_widget(PopupTest(name=''))
        return PopupTest()
#
# Name: Menu
# Description: メニュークラス
#
class Menu(BoxLayout):
    pass

#
# Name: AttendanceScreen
# Description: 出席管理画面クラス
#
class AttendanceScreen(Screen):
    def __init__(self, **kwargs):
        self.dt_now = datetime.datetime.now()
        self.weekday = ""
        if datetime.date.today().weekday() == 0:
            self.weekday = "月"
        elif datetime.date.today().weekday() == 1:
            self.weekday = "火"
        elif datetime.date.today().weekday() == 2:
            self.weekday = "水"
        elif datetime.date.today().weekday() == 3:
            self.weekday = "木"
        elif datetime.date.today().weekday() == 4:
            self.weekday = "金"
        elif datetime.date.today().weekday() == 5:
            self.weekday = "土"
        elif datetime.date.today().weekday() == 6:
            self.weekday = "日"
        else:
            self.weekday = " "

        self.date = f"{self.dt_now.strftime('%Y年%m月%d日 %H:%M:%S')} {self.weekday}曜日"
        self.controller = Controller()
        self.model = Model()
        self.counter = 0
        self.lectureInformation = self.model.lectureInformation.getAllInformation()
        self.lectureName = self.controller.lectureManager.searchLectureOfTheHourNow()
        super(AttendanceScreen, self).__init__(**kwargs)

    def getLectureName(self):
        return f'{self.lectureName}'

    def on_press(self):
        if self.lectureName != self.controller.lectureManager.searchLectureOfTheHourNow(): self.counter = 0
        if self.counter != 0 or self.lectureName=="ないです":
            self.ids.system_message.text = "ERROR"
            return
        self.dbname = "Lecture.db"
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(f'SELECT time FROM lectureInformation WHERE name=="{self.lectureName}"')

        list=[]
        while 1:
            i = cur.fetchone()
            if type(i)==type(None): break
            list.append(i[0])

        for j in list:
            time = re.split("[:~]",j)

            # 基準となる時間
            base1 = datetime.time(int(time[0]), int(time[1]), 0)

            dt1 = datetime.datetime.combine(datetime.date.today(), base1) + datetime.timedelta(minutes=15)
            dt2 = datetime.datetime.combine(datetime.date.today(), base1) + datetime.timedelta(minutes=30)

            # 現在時間
            dt_now = datetime.datetime.now()
            if dt_now <= dt1:
                self.controller.attendanceManager.addAttendanceInformation(self.lectureName,"出席")
            elif dt_now <= dt2:
                self.controller.attendanceManager.addAttendanceInformation(self.lectureName,"遅刻")
            else:
                self.controller.attendanceManager.addAttendanceInformation(self.lectureName,"欠席")

        cur.close()
        conn.close()

        self.counter = 1

#
# Name: TaskManagementScreen
# Description: 課題管理画面クラス
#
class TaskManagementScreen(Screen):
    def popup_open(self):
        content = PopupMenu1(popup_close=self.popup_close)
        self.popup = Popup(title='課題追加', content=content, size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.open()


    def popup_close(self):
        self.popup.dismiss()

    label_text = ObjectProperty(None)
    check = BooleanProperty(False)

    def checkbox_check(self, checkbox):
        self.check = checkbox.active
        return

    def label_text_change(self):
        if self.check == True:
            self.label_text.text = 'CheckBox is True'
        else:
            self.label_text.text = 'CheckBox is False'

class TestCheckBox(App):
    def build(self):
        root = TaskManagementScreen()
        return root

#
# Name: TaskViewScreen
# Description: 課題表示クラス
#
class TaskViewScreen(Screen):
    def calender(self,year,month):
        print(type(calendar.month(year, month)))

#
# Name: LectureManagerScreen
# Description: 講義管理画面クラス
#
class LectureManagerScreen(Screen):
    def __init__(self, **kwargs):
        self.model = Model()
        self.controller = Controller()

        self.lectureInformation = model.lectureInformation.getAll()

        print(self.lectureInformation)

        self.lname = []
        self.time = []
        self.counter = 0
        self.boxState = [0,0,0,0,0,0,0,0,0,0,0,0]
        for i in self.lectureInformation:
            print(i)
            if i[2] == "8:30~10:00": self.time.append(f'{i[2]}曜1限')
            elif i[2] == "10:20~11:50": self.time.append(f'{i[2]}曜2限')
            elif i[2] == "12:50~14:20": self.time.append(f'{i[2]}曜3限')
            elif i[2] == "14:40~16:10": self.time.append(f'{i[2]}曜4限')
            elif i[2] == "16:20~17:50": self.time.append(f'{i[2]}曜5限')
            else: self.time.append(f'{i[2]}曜?限')
            if i[0]!=" ":
                self.boxState[self.counter] = None
                self.lname.append(str(i[0]))
            else:
                self.lname.append(str(i[0]))
            self.counter += 1
            print(self.boxState)
            print(self.lname)
            print(self.time)

        super(LectureManagerScreen, self).__init__(**kwargs)

    def popup_open(self):
        content = PopupMenu2(popup_close=self.popup_close)
        self.popup = Popup(title='履修講義追加', content=content, size_hint=(0.7, 0.7), auto_dismiss=False)
        self.popup.open()

    def popup_close(self):
        self.popup.dismiss()

    def get(self):
        return self.time[0]

#
# Name: AssessmentScreen
# Description: 見込み評価画面クラス
#
class AssessmentScreen(Screen):
    def popup_open(self):
        content = PopupMenu3(popup_close=self.popup_close)
        self.popup = Popup(title='履修講義名', content=content, size_hint=(0.5, 0.5), auto_dismiss=True)
        self.popup.open()

    def popup_close(self):
        self.popup.dismiss()

#
# Name: View
# Description: メインメソッド
#
class View(App):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.title='StudentReminder'


    def build(self):
        # Create the screen manager

        # SM.add_widget(AttendanceScreen(name='attendance'))
        # return SM
        return Menu()

if __name__ == '__main__':
    View().run()