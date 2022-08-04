from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, BooleanProperty


class TextChanger(BoxLayout):
    label_text = ObjectProperty(None)
    check = BooleanProperty(False)

    def checkbox_check(self, checkbox):
        self.check = checkbox.active
        return

    #def label_text_change(self):
        #if self.check == True:
            #self.label_text.text = 'CheckBox is True'
        #else:
            #self.label_text.text = 'CheckBox is False'
    

class TestCheckBox(App):
    def build(self):
        root = TextChanger()
        return root


if __name__ == '__main__':
    TestCheckBox().run()