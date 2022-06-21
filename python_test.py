from kivy.uix.button import Button
from kivy.app import App

class MyApp(App):
    def build(self):
        return Button(text='Нажми если черный!')

if __name__=='__main__':
    MyApp().run()