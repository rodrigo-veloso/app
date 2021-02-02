#R Vemulapalli, A Agarwala, “A Compact Embedding for Facial Expression Similarity”, CoRR, abs/1811.11283, 2018.

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from app.show_figs import get_fig
from app.save_answer_mysql import save_answer
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.cache import Cache
from kivy.uix.textinput import TextInput
from app.username import check_username
from app.username import write_username
from app.user_query import user_check

class MyButton(Button):
  pass

class LearnerApp(App):

  dic_idade = {'-10':0,'10 a 18':1,'18 a 24':2,'25 a 34':3,'35 a 44':4,'45 a 64':5,' + 65':6}
  list_idade = ['-10','10 a 18','18 a 24','25 a 34','35 a 44','45 a 64','+ 65']
  dic_cabelo = {'preto':0,'loiro':1,'castanho':2,'ruivo':3,'branco':4,'outra':5}
  list_cabelo = ['preto','loiro','castanho','ruivo','branco','outra']
  dic_cor = {'preto':0,'pardo':1,'branco':2,'índigena':3,'amarelo':4}
  list_cor = ['preto','pardo','branco','índigena','amarelo']
  dic_genero = {'masculino':0,'feminino':1}
  list_genero = ['masculino','feminino']
  dic_sorrindo = {'Sim':0,'Não':1}
  list_sorrindo = ['Sim','Não']
  dic_acessorio = {'Sim':0,'Não':1}
  list_acessorio = ['Sim','Não']
  perguntas = ['Crie um nome de usuário:','Qual seu genero?','Qual sua cor/raça?','Qual sua idade?','Você foi cadastrado.','Avalie a beleza da pessoa de 0 a 10','Qual o genero?','Qual a cor/raça?','Qual a idade?','Qual a cor do cabelo?','Está sorrindo?','Usa chapéu ou óculos?','Obrigado por responder.']
  list_cols = [1,2,5,4,1,2,2,5,4,3,2,2]
  pages = 13
  
  def build(self):
    self.dic_master = {'idade':self.dic_idade,'cabelo':self.dic_cabelo,'genero':self.dic_genero,'sorrindo':self.dic_sorrindo,'cor':self.dic_cor,'acessorio':self.dic_acessorio}
    self.dic_list = {'idade':self.list_idade,'cabelo':self.list_cabelo,'genero':self.list_genero,'sorrindo':self.list_sorrindo,'cor':self.list_cor,'acessorio':self.list_acessorio}
    self.list_master = ['username','genero','cor','idade','','nota','genero','cor','idade','cabelo','sorrindo','acessorio']
    self.question_variables = {}
    self.user_variables = {}
    for variable in self.list_master[5:]:
      self.question_variables[variable] = 0
    for variable in self.list_master[:4]:
      self.user_variables[variable] = 0
    self.image_id, string = get_fig()
    self.question_variables['id'] = self.image_id
    self.question_variables['nota'] = 5
    check, username = check_username()
    if check:
      self.initial_page = 5
      self.question_variables['username'] = username 
    else:
      self.initial_page = 0
    self.pressed = None
    self.page_number = self.initial_page
    #string = 'imageToSaveRandom.png'
    self.sm = ScreenManager(transition=NoTransition())
    self.wimg_list = []
    for page in range(self.initial_page,self.pages):
      if page > 4:
        self.wimg_list.append(Image(source=string,size_hint_y = 10,width=300,allow_stretch=True,height=400,pos=(100,100)))
      else:
        self.wimg_list.append(Image(source='fig'+str(page)+'.png',size_hint_y = 10,width=400,allow_stretch=True,height=250,pos=(100,100)))
    for page in range(self.initial_page,self.pages):
      self.master_layout = GridLayout(cols=1)
      #if page > 3:
      self.master_layout.add_widget(self.wimg_list[page-self.initial_page])
      self.get_page(page)
      if page < self.pages - 1:
        if page == 0:
          self.master_layout.add_widget(Button(text='Próximo',on_press=self.user_check,size_hint_y=None,height=125))
        else:
          self.master_layout.add_widget(Button(text='Próximo',on_press=self.change_page,size_hint_y=None,height=125))
      else:
        self.final_button = Button(text='Avaliar outra pessoa',on_press=self.change_page,size_hint_y=None,height=150)
        self.master_layout.add_widget(self.final_button)
      screen = Screen(name=str(page))
      screen.add_widget(self.master_layout)
      self.sm.add_widget(screen)
    return self.sm

  def change_page(self,instance):
    if self.pressed != None or self.page_number == 0 or self.page_number == 4 or self.page_number == 5 or self.page_number == self.pages-1:
      if self.page_number < self.pages-1:
        if self.page_number != 0 and self.page_number != 4 and self.page_number != 5:
          self.pressed.background_color = (1,1,1,1)
          self.pressed = None
        if self.page_number == 4:
          #print(self.user_variables)
          save_answer(self.user_variables,"users")
          write_username(self.user_variables['username'])
        self.page_number+=1
        self.sm.current = str(self.page_number)
      elif self.page_number == self.pages-1:
        self.page_number = 5
        self.sm.current = str(self.page_number)
        print(self.question_variables)
        save_answer(self.question_variables,"labels")
        self.image_id, string = get_fig()
        self.question_variables['id'] = self.image_id
        for wimg in self.wimg_list:
          wimg.reload()
        self.question_variables['nota'] = 5
    
  def get_parameter(self,instance):
    if self.pressed != None:
        self.pressed.background_color = (1,1,1,1)
    instance.background_color = (1,0,0,1)
    self.pressed = instance
    if self.page_number > 4:
      self.question_variables[self.list_master[self.page_number]] = self.dic_master[self.list_master[self.page_number]][instance.text]
    else:
      self.user_variables[self.list_master[self.page_number]] = self.dic_master[self.list_master[self.page_number]][instance.text]
  #def change_button_color(self)
    
  def value_change(self,instance,value):
    self.slide_label.text = f'{value:.1f}'
    self.question_variables['nota'] = value  
    print(value)

  def user_check(self, instance):
    if user_check(self.user_variables['username']):
      self.change_page(instance)
    else:
      self.label1.text = 'Nome já cadastrado, tente outro.'

  def set_page(self,page):
    self.label=Label(text=self.perguntas[page],size_hint_y=None,height=90)
    self.layout = GridLayout(cols=self.list_cols[page],size_hint_y=None,height=125)
    for var in self.dic_master[self.list_master[page]]:
      self.layout.add_widget(Button(text=var,on_press=self.get_parameter, height = 60))
    self.master_layout.add_widget(self.label)
    self.master_layout.add_widget(self.layout)

  def on_text(self, instance, value):
    self.user_variables['username'] = value
    self.question_variables['username'] = value    

  def get_page(self,page):
    if page == 0:
      self.label1=Label(text=self.perguntas[0],size_hint_y=None,height=90)
      self.textinput = TextInput(text='', multiline=False,size_hint_y=None,height=100)
      self.textinput.bind(text=self.on_text)
      self.master_layout.add_widget(self.label1)
      self.master_layout.add_widget(self.textinput)
    elif page == 4:
      self.label=Label(text='Cadastro concluído.',size_hint_y=None,height=90)
      self.master_layout.add_widget(self.label)
    elif page == 5:
      self.label=Label(text='Avalie a aparência da pessoa de 0 a 10',size_hint_y=None,height=90)
      self.layout = GridLayout(cols=2,size_hint_y=None,height=125)
      self.slider = Slider(min=0,max=10,value=5,value_track=True,value_track_color=[1, 0, 0, 1])
      self.layout.add_widget(self.slider)
      self.slider.bind(value = self.value_change)
      self.slide_label = Label(text = "5")
      self.layout.add_widget(self.slide_label)
      self.master_layout.add_widget(self.label)
      self.master_layout.add_widget(self.layout)
    elif page == 12:
      self.label=Label(text='Obrigado por responder.',size_hint_y=None,height=90)
      self.master_layout.add_widget(self.label)
    else:
      self.set_page(page)

if __name__ == '__main__':
  LearnerApp().run()
