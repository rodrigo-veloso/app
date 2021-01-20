from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image

class MyButton(Button):
  pass

class LearnerApp(App):
  def build(self):
    #return MyButton(text='Opition 1')
    wimg = Image(source='figs/00001.png')
    return wimg

if __name__ == '__main__':
  LearnerApp().run()
