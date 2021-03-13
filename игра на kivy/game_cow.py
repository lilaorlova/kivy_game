from kivy.app import App
from kivy.clock import Clock
from kivy.uix.stacklayout import StackLayout
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.uix.popup import Popup
from datetime import datetime
import os
import ast
import time
import pickle
import random
from normproga import check
from normproga import unique_list
from kivy.config import Config
from kivy.core.window import Window
Window.clearcolor = [.95, .82, .57, 1]
file = 'file_words.pk'
with open(file, 'wb') as fi:
    pickle.dump(time.time(),fi)
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 2000)
Config.set('graphics', 'height', 2000)

class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        box = FloatLayout(size = (300, 300))
        box.add_widget(Button(text='Быки и коровы',
                            font_size = 70, 
                            color = [0, 0, 0, 1],
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (360, 500)))
        box.add_widget(Button(text='Правила для чайников',
                            font_size = 25, 
                            background_color = [.96, .38, .31, 1],
                            background_normal = '',
                            size_hint = (.5, .25),
                            pos = (200, 250),
                            on_press=lambda x: set_screen('rools')))
        box.add_widget(Button(text='Начало',
                            font_size = 25,
                            background_color = [.96, .38, .31, 1], 
                            background_normal = '',
                            size_hint = (.5, .25),
                            pos = (200, 50),
                            on_press=lambda x: set_screen('menu')))
        self.add_widget(box)

class MenuScreen2(Screen):
    def __init__(self, **kw):
        
        super(MenuScreen2, self).__init__(**kw)
        box = FloatLayout(size = (300, 300))
        box.add_widget(Button(text='Выберите кол-во букв в слове',
                            font_size = 30, 
                            color = [0, 0, 0, 1], 
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (360, 160),
                            on_press=lambda x: set_screen('rools')))
        box.add_widget(Button(text='Играть',
                            font_size = 60,
                            background_color = [.96, .38, .31, 1], 
                            background_normal = '',
                            size_hint = (.5, .25),
                            pos = (200, 260),
                            on_press=self.callback_press,
                            on_release=lambda x: set_screen('add_food')
                            ))

        self.a1=ToggleButton(text='2',background_color = [.96, .38, .31, 1], 
                            background_normal = '', group='some',size_hint=(.10, .10),pos=(86, 50))
        self.a2=ToggleButton(text='3',background_color = [.96, .38, .31, 1], 
                            background_normal = '', group='some',size_hint=(.10, .10),pos=(186, 50))
        self.a3=ToggleButton(text='4',background_color = [.96, .38, .31, 1], 
                            background_normal = '', group='some',size_hint=(.10, .10), pos=(286, 50),state='down')
        self.a4=ToggleButton(text='5',background_color = [.96, .38, .31, 1], 
                            background_normal = '', group='some',size_hint=(.10, .10),pos=(386, 50))
        self.a5=ToggleButton(text='6',background_color = [.96, .38, .31, 1], 
                            background_normal = '', group='some',size_hint=(.10, .10),pos=(486, 50))#,state='normal')
        self.a6=ToggleButton(text='7',background_color = [.96, .38, .31, 1], 
                            background_normal = '', group='some',size_hint=(.10, .10), pos=(586, 50))#,state='normal')
        self.a7=ToggleButton(text='8',background_color = [.96, .38, .31, 1], 
                            background_normal = '', group='some',size_hint=(.10, .10),pos=(686, 50))#,state='down')
        box.add_widget(self.a1)
        box.add_widget(self.a2)
        box.add_widget(self.a3)
        box.add_widget(self.a4)
        box.add_widget(self.a5)
        box.add_widget(self.a6)
        box.add_widget(self.a7)
        self.some=[]
        self.some.append(self.a1)
        self.some.append(self.a2)
        self.some.append(self.a3)
        self.some.append(self.a4)
        self.some.append(self.a5)
        self.some.append(self.a6)
        self.some.append(self.a7)
        self.add_widget(box)

    def callback_press(self, inctance):
        for nomber in self.some:
            if nomber.state=='down':
                file = 'file.pk'
                with open(file, 'rb') as fi:
                    WordList = pickle.load(fi)
                    choice_word=random.choice(WordList)
                    while(len(choice_word)!=int(nomber.text)):
                        choice_word=random.choice(WordList)
                    print(choice_word , nomber.text)
                    with open('file_choice_word.pk', 'wb') as fi:
                        pickle.dump(choice_word,fi)

class SortedListFood(Screen):
    def __init__(self, **kw):
        super(SortedListFood, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана

        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Назад к игре',
                             on_press=lambda x: set_screen('add_food'),
                             size_hint_y=None, height=dp(40))
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)

        dic_foods = ast.literal_eval(
            App.get_running_app().config.get('General', 'user_data'))
        file = 'file_words.pk'
        with open(file, 'rb') as fi:
            time = pickle.load(fi)
        for f, d in sorted(dic_foods.items(), key=lambda x: x[1]):
            fd = f.decode('u8')
            if time>d:
                pass
            else:
                btn = Button(text=fd, size_hint_y=None, height=dp(40))
                self.layout.add_widget(btn)
    def on_leave(self):  # Будет вызвана в момент закрытия экрана

        self.layout.clear_widgets()  # очищаем список


class AddFood(Screen):

    def buttonClicked(self, btn1):
        if self.check==0:
            file = 'file_choice_word.pk'
            with open(file, 'rb') as fi:
                self.choice_word = pickle.load(fi)
            self.check+=1
        else:
            pass
        if not self.txt1.text:
            return
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'user_data'))
        self.app.user_data[self.txt1.text.encode('u8')] = int(time.time())

        self.app.config.set('General', 'user_data', self.app.user_data)
        self.app.config.write()

        cout = check(self.choice_word,self.txt1.text)
        text = 'Коровы- '+str(cout[0])+' Быки- '+str(cout[-1])
        print(self.choice_word, check(self.choice_word,self.txt1.text), self.txt1.text)
        if cout[-1]==len(self.choice_word):

            self.callback_press(1)
        else:
            self.i+=1
            if len(self.txt1.text)>len(self.choice_word) or len(self.txt1.text)<len(self.choice_word):
                some="Надо ввести слово с таким-же количеством букв \n"
            else:
                some = str(self.i)+' '+self.txt1.text+":  "+text+'\n'
            self.some_text.append(some)

        self.result.text =' '.join(self.some_text)
        self.txt1.text = ''

    def callback_press(self, inctance):
        self.popup=Popup(title='',auto_dismiss=False)# , size=(300, 300), size_hint=(None, None))
        if inctance==1:
            self.popup.add_widget(Button(text="ВЫ ПОБЕДИЛИ\n \n"+"Слово: "+self.choice_word+'\n \n нажмите что бы выйти на главный экран',font_size = 30, 
                                background_color = [0.7, 0.5, 0.8, 1], 
                                
                                on_press = lambda x: set_screen('menu'), 
                                on_release=self.on_release))
        else:
            self.popup.add_widget(Button(text="Слово: "+self.choice_word+'\n \n нажмите что бы выйти на главный экран',font_size = 30, 
                                background_color =[.95, .82, .57, 1], 
                                
                                on_press = lambda x: set_screen('menu'), 
                                on_release=self.on_release))
   #                         popup.dismiss()))
        self.popup.open()

    def on_release(self, inctance):
        self.some_text=[]
        self.check=0
        self.popup.dismiss()
  #      self.choice_word=random.choice(WordList)
  #      while( self.slider.value!= len(self.choice_word)):
   #         self.choice_word=random.choice(WordList)
    def __init__(self, **kw):
        self.some_text=[]
        self.i= 0
        self.check=0
        WordList=[]
        file = 'file_choice_word.pk'
        with open(file, 'rb') as fi:
            self.choice_word = pickle.load(fi)
        super(AddFood, self).__init__(**kw)


        box = FloatLayout(size = (300, 300))   
        self.txt1 = TextInput(text='', multiline=False, font_size = 16, 
                            size_hint = (1, .10),
                            pos = (0, 540), hint_text="Ваше слово")
        box.add_widget(self.txt1)
        btn1 = Button(text="Добавить слово",font_size = 16, 
                            background_color = [.96, .38, .31, 1], 
                            background_normal = '',
                            size_hint = (1, .10),
                            pos = (0, 500),size_hint_y=None, height=dp(40))
        btn1.bind(on_press=self.buttonClicked)
        box.add_widget(btn1)
        self.result = Label(text='', color = [0, 0, 0, 1],font_size = 20)
        box.add_widget(self.result)
        self.add_widget(box)

        """ box.add_widget(Button(text='Все добавленные вами слова', 
                            font_size = 16, 
                            background_color = [0.7, 0.5, 0.8, 1], 
                            background_normal = '',
                            size_hint = (.5, .10),
                            pos = (0, 460),on_press=lambda x: set_screen('list_food'), size_hint_y=None, height=dp(40)))"""
               
        back_button = Button(text='Сдаться', 
                            font_size = 40, 
                            background_color = [.96, .38, .31, 1], 
                            background_normal = '',
                            size_hint = (.3, .1),
                            pos = (0, 0),
                            on_press=self.callback_press)
                           # set_screen('menu'))
        box.add_widget(back_button)
        
class Rools(Screen):
       
    def __init__(self, **kw):
        super(Rools, self).__init__(**kw)
        box = FloatLayout(size = (300, 300))
        back_button = Button(text='<-', 
                            font_size = 60, 
                            color = [0, 0, 0, 1],
                            background_color = [.96, .38, .31, 1], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (0, 0),
                            on_press=lambda x:
                            set_screen('menu'))
        box.add_widget(back_button)
        self.txt1 = Button(text='В классическом варианте игра рассчитана на двух игроков, \n       но в нашем варианте вы будете играть с компьютером.',
                            font_size = 16, 
                            color = [0, 0, 0, 1],
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (370,420))
        self.txt2 = Button(text = '    Компьютер задумывает и записывает тайное 4-значное слово. \n                    Игрок делает первую попытку отгадать слово.',
                            font_size = 16, 
                            color = [0, 0, 0, 1],
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (370,385))
        self.txt3 = Button(text = '             Попытка — это ваше слово, записанное в выделенное окошко.',

                            font_size = 16, 
                            color = [0, 0, 0, 1],
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (350,360)) 
        self.txt4 = Button(text = 'Компьютер сообщает в ответ, сколько букв угадано без совпадения с их позициями в тайном числе \n                                                    (то есть количество коров) и сколько угадано \n                                    вплоть до позиции в тайном слове(то есть количество быков).',

                            font_size = 16, 
                            color = [0, 0, 0, 1],
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (370,320))  
        self.txt5 = Button(text = 'Например:Задумано тайное слово «дом».',

                            font_size = 16, 
                            color = [0, 0, 0, 1],
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (370,280))   
        self.txt6 = Button(text = 'Попытка: «ком».Результат: два «быка» (две буквы: «о» и «м» — угаданы на верных позициях) \n                                    и ноль «коров» (остальные буквы никак не совпадают).',

                            font_size = 16, 
                            color = [0, 0, 0, 1],
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (370,250)) 
        self.txt7 = Button(text = ' Игрок побеждает тогда, когда отгадает слово.',

                            font_size = 16, 
                            color = [0, 0, 0, 1],
                            background_color = [0, 0, 0, 0], 
                            background_normal = '',
                            size_hint = (.1, .1),
                            pos = (370,220))                                            
        box.add_widget(self.txt1)
        box.add_widget(self.txt2)
        box.add_widget(self.txt3)
        box.add_widget(self.txt4)
        box.add_widget(self.txt5)
        box.add_widget(self.txt6)
        box.add_widget(self.txt7)
        self.result = Label(text='')
        box.add_widget(self.result)
        self.add_widget(box)
        


def set_screen(name_screen):
    sm.current = name_screen
    
    


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu2'))
sm.add_widget(Rools(name='rools'))
sm.add_widget(AddFood(name='add_food'))
sm.add_widget(SortedListFood(name='list_food'))
sm.add_widget(MenuScreen2(name='menu'))



class WordOptionsApp(App):
    def __init__(self, **kvargs):
        super(WordOptionsApp, self).__init__(**kvargs)
        self.config = ConfigParser()

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'user_data', '{}')

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'user_data'))

    def get_application_config(self):
        return super(WordOptionsApp, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))

    def build(self):
        return sm


if __name__ == '__main__':
    WordOptionsApp().run()
    