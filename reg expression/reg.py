from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ChildApp(GridLayout):
    def __init__(self):
        super(ChildApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.add_widget(Label(text='student Marks'))
        self.s_Marks = TextInput()
        self.add_widget(self.s_Marks)

        self.add_widget(Label(text='Age'))
        self.s_Age = TextInput()
        self.add_widget(self.s_Age)

        self.press = Button(text='click me')
        self.add_widget(self.press)


class ParentApp(App):
    def build(self):
        return ChildApp()


if __name__ == "__main__":
    ParentApp().run()
