from ctypes.wintypes import SMALL_RECT
import datetime
from modulefinder import Module
from select import select
from tokenize import String

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

####日本語対応用コード
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分
resource_add_path('/System/Library/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'Hiragino Sans GB.ttc')  # 追加分
####日本語対応ここまで

#ウィンドウサイズの定義
Config.set('graphics', 'width', 1600)
Config.set('graphics', 'height', 800)
Config.set('graphics', 'resizable', 0)

#
# Name: Menu
# Description: メニュークラス
#
class Menu(BoxLayout):
    pass

#
# Name: AttendanceScreen
# Description: 出席管理スクリーンクラス
#
class AttendanceScreen(Screen):
    def __init__(self, **kwargs):
        super(AttendanceScreen, self).__init__(**kwargs)

#
# Name: TaskManagementScreen
# Description: 課題管理スクリーンクラス
#
class TaskManagementScreen(Screen):
    pass

#
# Name: TaskViewScreen
# Description: 課題表示クラス
#
class TaskViewScreen(Screen):
    pass

class LectureManagerScreen(Screen):
    pass

class AssessmentScreen(Screen):
    pass

#
# Name: View
# Description: メインメソッド
#
class View(App):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.title='DENCHU'


    def build(self):
        # Create the screen manager

        # SM.add_widget(AttendanceScreen(name='attendance'))
        # return SM
        return Menu()

if __name__ == '__main__':
    View().run()