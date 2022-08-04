from ctypes.wintypes import SMALL_RECT
import datetime
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
        self.popup = Popup(title='Popup Test', content=content, size_hint=(0.5, 0.5), auto_dismiss=False)
        self.popup.open()

class PopupTest(Screen):
    def popup_open(self):
        content = PopupMenu2(popup_close=self.popup_close)
        self.popup = Popup(title='Popup Test', content=content, size_hint=(0.5, 0.5), auto_dismiss=False)
        self.popup.open()

class PopupTest(Screen):
    def popup_open(self):
        content = PopupMenu3(popup_close=self.popup_close)
        self.popup = Popup(title='Popup Test', content=content, size_hint=(0.5, 0.5), auto_dismiss=False)
        self.popup.open()

    def popup_close(self):
        self.popup.dismiss()


class PopupApp(App):
    def build(self):
        sm.add_widget(PopupTest(name='popupTest'))
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
        self.date = f"{self.dt_now.strftime('%Y年%m月%d日 %H:%M:%S')}"
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
        self.popup = Popup(title='Popup Test', content=content, size_hint=(0.5, 0.5), auto_dismiss=False)
        self.popup.open()

    def popup_close(self):
        self.popup.dismiss()

#
# Name: TaskViewScreen
# Description: 課題表示クラス
#
class TaskViewScreen(Screen):
    pass

#
# Name: LectureManagerScreen
# Description: 講義管理画面クラス
#
class LectureManagerScreen(Screen):
    def popup_open(self):
        content = PopupMenu2(popup_close=self.popup_close)
        self.popup = Popup(title='Popup Test', content=content, size_hint=(0.5, 0.5), auto_dismiss=False)
        self.popup.open()

    def popup_close(self):
        self.popup.dismiss()

#
# Name: AssessmentScreen
# Description: 見込み評価画面クラス
#
class AssessmentScreen(Screen):
    def popup_open(self):
        content = PopupMenu3(popup_close=self.popup_close)
        self.popup = Popup(title='Popup Test', content=content, size_hint=(0.5, 0.5), auto_dismiss=False)
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