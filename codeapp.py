from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from app.show_figs import get_fig

class MyButton(Button):
  pass

class LearnerApp(App):
  def build(self):
    #return MyButton(text='Opition 1')
    print(get_fig())
    wimg = Image(source="app/imageToSaveRandom.png")
    return wimg

if __name__ == '__main__':
  LearnerApp().run()
