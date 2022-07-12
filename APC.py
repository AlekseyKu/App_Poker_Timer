from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
# from kivy.clock import Clock
from kivy.uix.button import Button
# from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.base import runTouchApp
import time
import threading
from kivy.properties import StringProperty, ListProperty
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView

# from PIL import Image

Window.size = (360, 640)
Builder.load_file('APC_settings.kv')
Builder.load_file('Classic_tournament.kv')

round_minutes = 0

global_num_round = NumericProperty(0)


class BtnControl(Button):
    pass


class WidgetTournamentCat(BoxLayout):
    orientation = 'vertical'

    def widget_construction(self):
        rw_boxlayout = BoxLayout(orientation="horizontal")

        rw_label_num_round = Label(text=self.label_num_round, size_hint_x=0.25) # pos_hint={'right': 0})
        # rw_button_m_blind = Button(text='-', size_hint_x=0.13)
        rw_label_m_blind = Label(text=self.label_m_blind, size_hint_x=0.10)
        rw_label_article = Label(text='/', size_hint_x=0.04)
        rw_label_b_blind = Label(text=self.label_b_blind, size_hint_x=0.10)
        # rw_button_b_blind = Button(text='+', size_hint_x=0.13)
        rw_label_blinds = Label(text='blinds', size_hint_x=0.25)

        # rw_button_m_blind.bind(on_press=self.clicker_func)
        # rw_button_m_blind.bind(on_press=self.button_down_blind)
        sm.get_screen('menu').ids.menu_m_blind_id.text = self.label_m_blind

        # rw_button_b_blind.bind(on_press=self.method)
        # rw_button_b_blind.bind(on_press=self.button_up_blind)
        sm.get_screen('menu').ids.menu_b_blind_id.text = self.label_b_blind

        self.add_widget(rw_boxlayout)
        rw_boxlayout.add_widget(rw_label_num_round)
        # self.add_widget(rw_button_m_blind)
        rw_boxlayout.add_widget(rw_label_m_blind)
        rw_boxlayout.add_widget(rw_label_article)
        rw_boxlayout.add_widget(rw_label_b_blind)
        # self.add_widget(rw_button_b_blind)
        rw_boxlayout.add_widget(rw_label_blinds)

    def round_1(self):
        self.label_num_round = 'round ' + str(self.num_round[0])

        self.m_blind = self.list_blinds[0]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_2(self):
        self.label_num_round = 'round ' + str(self.num_round[1])

        self.m_blind = self.list_blinds[1]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_3(self):
        self.label_num_round = 'round ' + str(self.num_round[2])

        self.m_blind = self.list_blinds[2]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_4(self):
        self.label_num_round = 'round ' + str(self.num_round[3])

        self.m_blind = self.list_blinds[3]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_5(self):
        self.label_num_round = 'round ' + str(self.num_round[4])

        self.m_blind = self.list_blinds[4]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_6(self):
        self.label_num_round = 'round ' + str(self.num_round[5])

        self.m_blind = self.list_blinds[5]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_7(self):
        self.label_num_round = 'round ' + str(self.num_round[6])

        self.m_blind = self.list_blinds[6]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_8(self):
        self.label_num_round = 'round ' + str(self.num_round[7])

        self.m_blind = self.list_blinds[7]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_9(self):
        self.label_num_round = 'round ' + str(self.num_round[8])

        self.m_blind = self.list_blinds[8]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def round_10(self):
        self.label_num_round = 'round ' + str(self.num_round[9])

        self.m_blind = self.list_blinds[9]
        self.label_m_blind = str(self.m_blind)

        self.b_blind = self.m_blind * 2
        self.label_b_blind = str(self.b_blind)

        self.widget_construction()

    def __init__(self, **kwargs):
        super(WidgetTournamentCat, self).__init__(**kwargs)

        # self.num_round = [1, 2, 3]
        self.num_round = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

        # self.list_blinds = [5, 10, 15]
        self.list_blinds = [5, 10, 15, 25, 50, 75, 100, 150, 250, 500, 750, 1000, 1500, 2000, 2500, 5000]

        self.round_1()
        self.round_2()
        self.round_3()
        self.round_4()
        self.round_5()
        self.round_6()
        self.round_7()
        self.round_8()
        self.round_9()
        self.round_10()

        '''
        for index in self.num_round:
            if index == 1:
                self.label_num_round = 'round ' + str(self.num_round[0])
                self.m_blind = self.list_blinds[0]
                self.b_blind = self.m_blind * 2
                self.widget_construction()
                print(self.m_blind)
            else:
                self.next = index
                self.label_num_round = 'round ' + str(self.next)
                self.m_blind = self.list_blinds[0+1]
                self.b_blind = self.m_blind * 2
                print(self.m_blind)
                self.widget_construction()
        '''
class WidgetTournamentCt(BoxLayout):
    label_num_round = StringProperty()
    label_m_blinds = StringProperty()
    label_b_blinds = StringProperty()
    # self.num_round = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    # self.list_blinds = [5, 10, 15, 25, 50, 75, 100, 150, 250, 500, 750, 1000, 1500, 2000, 2500, 5000]
    num_round = [1, 2, 3]
    list_blinds = [5, 10, 15]

    def __init__(self, **kwargs):
        super(WidgetTournamentCt, self).__init__(**kwargs)

        for index in self.num_round:
            print(index)
            self.label_num_round = 'round ' + str(self.num_round[0])

            m_blind = self.list_blinds[0]
            self.label_m_blinds = str(self.list_blinds[0])
            self.label_b_blinds = str(m_blind * 2)





class RoundWidgetNew(BoxLayout):
    # global len_round

    def clicker_func(self, event):
        pass

    def __init__(self, **kwargs):
        super(RoundWidgetNew, self).__init__(**kwargs)
        pass
        ## super().__init__(**kwargs)
        ## self.a = SettingsScreen()
        ## self.r_round = len(self.ids.Round_Widget_id.children)
        ## print(self.a.num_of_widgets())

        ##self.len_round = len(self.ids.Round_Widget_id.children)
        ##num_round = 'round' + str(self.len_round)

        self.list_m_blinds = [5, 10, 15, 25, 50, 75, 100, 150, 250, 500, 750, 1000, 1500, 2000, 2500, 5000]

        self.m_blind = self.list_m_blinds[0]
        self.b_blind = self.m_blind * 2

        self.label_m_blind = str(self.m_blind)
        self.label_b_blind = str(self.b_blind)

        rw_label_num_round = Label(text="num_round", size_hint_x=0.25)  # pos_hint={'right': 0})
        rw_button_m_blind = Button(text='-', size_hint_x=0.13)
        rw_label_m_blind = Label(text=self.label_m_blind, size_hint_x=0.10)
        rw_label_article = Label(text='/', size_hint_x=0.04)
        rw_label_b_blind = Label(text=self.label_b_blind, size_hint_x=0.10)
        rw_button_b_blind = Button(text='+', size_hint_x=0.13)
        rw_label_blinds = Label(text='blinds', size_hint_x=0.25)

        rw_button_m_blind.bind(on_press=self.clicker_func)
        rw_button_m_blind.bind(on_press=self.button_down_blind)
        sm.get_screen('menu').ids.menu_m_blind_id.text = self.label_m_blind

        rw_button_b_blind.bind(on_press=self.method)
        rw_button_b_blind.bind(on_press=self.button_up_blind)
        sm.get_screen('menu').ids.menu_b_blind_id.text = self.label_b_blind

        self.add_widget(rw_label_num_round)
        self.add_widget(rw_button_m_blind)
        self.add_widget(rw_label_m_blind)
        self.add_widget(rw_label_article)
        self.add_widget(rw_label_b_blind)
        self.add_widget(rw_button_b_blind)
        self.add_widget(rw_label_blinds)

    ##def logic(self):

    ##self.label_m_blind.text = self.m_blind
    ##self.label_b_blind.text = self.b_blind

    def button_down_blind(self, m_blind):
        down_blind = self.m_blind
        self.m_blind = self.list_m_blinds[1]

        print(self.m_blind)
        return down_blind

    def button_up_blind(self, m_blind):
        # up_blind = self.list_m_blinds[1]
        self.m_blind = self.list_m_blinds[3]
        self.b_blind = self.m_blind * 2
        print(self.label_m_blind)
        print(self.label_b_blind)
        self.logic()
        sm.get_screen('menu').ids.menu_m_blind_id.text = self.label_m_blind
        sm.get_screen('menu').ids.menu_b_blind_id.text = self.label_b_blind
        return self.label_m_blind

    def method(self, event):
        pass
        # print(self.a.num_of_widgets())
        # print(self.r_round)


class RoundWidget(BoxLayout):
    number_rounds = "round"
    '''##
    def __init__(self):
        r_round = len(self.ids.Round_Widget_id.children)
    def method(self):
        t_round = str(r_round)
        return t_round
    '''

    ''' 
    #ss = SettingsScreen()
    #ss.RoundWidget()
    #number_rounds = 'round'
    number_rounds = StringProperty()
    def print_label(self):
        print(self.number_rounds)
        print('it')
    def amount(self):
        r_round = len(self.ids.Round_Widget_id.children)
        #global t_round
        t_round = str(r_round)
        self.number_rounds = t_round
        return self.number_rounds
    pass
    def round_testing(self):
        self.ids['rw_label'].text = str(number_rounds)
    '''


class TestLabel(Label):
    pass


'''
class TourSpinner(Spinner):
    def spinner_cat(self):
        print('cat')
    def spinner_ft(self):
        print('ft')
    def spinner_ct(self):
        print('ct')
'''


class Main:

    def round_minutes_func(self):
        t = round_minutes * 60

        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # self.ids['lbl_round_minutes'].text = str(round_minutes)
        sm.get_screen('settings').ids.lbl_round_minutes.text = str(round_minutes)
        sm.get_screen('menu').ids.lbl_round_minutes_main.text = str(timer)
        print(timer)
        return timer

    def round_minutes_plus(self):
        global round_minutes

        if round_minutes >= 0:
            round_minutes += 1
            self.round_minutes_func()

    def round_minutes_minus(self):
        global round_minutes

        if round_minutes > 0:
            round_minutes -= 1
            self.round_minutes_func()


class Num(Main):
    pass

    # передача результата в kv-файл
    # self.ids['lbl_round_minutes_main'].text = str(self.round_minutes)
    # sm.get_screen('menu').ids.lbl_round_minutes_main.text = str(self.round_minutes)


##########################################################################

class MenuScreen(Num, Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        ...
        self.event = threading.Event()

        self.thread_flag = None
        self.stop_flag = False
        print(threading.enumerate())

    def logic_time(self):
        t = round_minutes * 60

        while t:
            self.event.wait()

            mins, secs = divmod(t, 60)
            self.timer = '{:02d}:{:02d}'.format(mins, secs)
            print(self.timer, end="\r")
            print(t)
            time.sleep(1)
            t -= 1
            print(self.timer)
            sm.get_screen('menu').ids.lbl_round_minutes_main.text = str(self.timer)
            if t == 0:
                time.sleep(1)
                sm.get_screen('menu').ids.lbl_round_minutes_main.text = str('TIME IS UP')
                self.event.clear()

                print(threading.enumerate())
                print('STOP')

    def logic_time_start(self):
        while True:
            self.event.wait()
            self.logic_time()

    def thread_start(self):

        if not self.stop_flag:
            threading.Thread(target=self.logic_time_start).start()
            self.event.set()
            print(threading.enumerate())
        else:
            print('else')
            self.event.set()
            # self.ids.button_start.disable = True
            print(threading.enumerate())

    def thread_pause(self):
        self.event.clear()
        self.stop_flag = True
        # self.ids.button_start.disable = True
        print(threading.enumerate())

    def resume(self):
        self.event.set()

    def button_start_disable(self):
        self.ids.button_start.disabled = True
        self.ids.button_pause.disabled = False
        self.ids.button_start_normal.source = 'icon/play_on_c.png'
        self.ids.button_pause_normal.source = 'icon/pause.png'

    def button_pause_disable(self):
        self.ids.button_start.disabled = False
        self.ids.button_pause.disabled = True
        self.ids.button_pause_normal.source = 'icon/pause_on_c.png'
        self.ids.button_start_normal.source = 'icon/play.png'

    def button_settings(self):
        if self.thread_flag == True:
            # Factory.Settings_Popup().open()
            print('RUN')
        else:
            print('time is up')


##########################################################################

class SettingsScreen(Screen, Num):
    num_rounds = 0

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

    def num_rounds_plus(self):
        self.num_rounds += 1
        self.add_rounds()

    def num_rounds_minus(self):
        if self.num_rounds > 0:
            self.num_rounds -= 1
            self.del_rounds()

        else:
            pass

    def logic_num_rounds_and_blinds(self):
        pass

    def add_rounds(self):
        pass

        ## op
        ## self.ids.Round_Widget_id.add_widget(RoundWidget(size_hint_y=0.5, pos_hint={'top': 1}))

        self.ids.Round_Widget_id.add_widget(RoundWidgetNew(size_hint_y=0.5, pos_hint={'top': 1}))

    def del_rounds(self):
        pass

        self.ids.Round_Widget_id.remove_widget(self.ids.Round_Widget_id.children[0])
        ## print(self.ids.Round_Widget_id.children)
        ## print(self.num_of_widgets())

    def num_of_widgets(self):
        num_of_e = len(self.ids.Round_Widget_id.children)
        return num_of_e

    def dialog_dismiss(self):
        self.dialog_dismiss()

    def spinner_func(self, value):
        if value == 'classic Arizona tournament':
            # print('cAt')
            self.tournament_cat()

        elif value == 'fast tournament':
            self.tournament_ft()

        elif value == 'custom tournament':
            print('ct')

        else:
            pass

    def tournament_cat(self):
        global round_minutes
        round_minutes = 15
        Main().round_minutes_func()

        if self.ids.Round_Widget_id.children:
            self.ids.Round_Widget_id.remove_widget(self.ids.Round_Widget_id.children[0])
        self.ids.Round_Widget_id.add_widget(WidgetTournamentCat(size_hint_y=0.5, pos_hint={'top': 1}))

    def tournament_ft(self):
        global round_minutes
        round_minutes = 10
        Main().round_minutes_func()

        if self.ids.Round_Widget_id.children:
            self.ids.Round_Widget_id.remove_widget(self.ids.Round_Widget_id.children[0])
        self.ids.Round_Widget_id.add_widget(WidgetTournamentCt(size_hint_y=0.5, pos_hint={'top': 1}))

        '''
        rounds = 1
        while rounds < 4:
            print(rounds)
            self.ids.Round_Widget_id.add_widget(WidgetTournamentCat(size_hint_y=0.5, pos_hint={'top': 1}))
            rounds = rounds+1
        '''


class Manager(ScreenManager):
    pass
    # self.ids['lbl_round_minutes_main'].text = str(self.timer)
    # sm.get_screen('menu').ids.lbl_round_minutes_main.text = str(self.timer)


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))


class APCApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    APCApp().run()

# https://ru.stackoverflow.com/questions/1012335/%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%B0%D1%87%D0%B0-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D1%85-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-%D0%BE%D0%BA%D0%BD%D0%B0%D0%BC%D0%B8-%D0%B2-python-kivy
