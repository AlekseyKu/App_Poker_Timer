from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
#from kivy.clock import Clock
from kivy.uix.button import Button
#from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.base import runTouchApp
import time
import threading
from kivy.properties import StringProperty, ListProperty

#from PIL import Image

Window.size = (360, 640)
Builder.load_file('APC_settings.kv')


class BtnControl(Button):
    pass


class RoundWidget(BoxLayout):
    h = "round"
    pass


class TestLabel(Label):
    pass


round_minutes = 0
test_num = 4


class Main:

    def round_minutes_plus(self):
        global round_minutes

        if round_minutes >= 0:
            round_minutes += 1
            t = round_minutes * 60

            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.ids['lbl_round_minutes'].text = str(round_minutes)
            sm.get_screen('menu').ids.lbl_round_minutes_main.text = str(timer)
            print(timer)
            return timer

    def round_minutes_minus(self):
        global round_minutes

        if round_minutes > 0:
            round_minutes -= 1
            t = round_minutes * 60

            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.ids['lbl_round_minutes'].text = str(round_minutes)
            sm.get_screen('menu').ids.lbl_round_minutes_main.text = str(timer)
            # print(self.ids.lbl_round_minutes.text)
            print(timer)
            return timer


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
        print(self.num_rounds)
        self.add_rounds()

    def num_rounds_minus(self):
        if self.num_rounds > 0:
            self.num_rounds -= 1
            print(self.num_rounds)
            self.del_rounds()
        else:
            pass

    def add_rounds(self):
        # for i in range(self.num_rounds):

        self.ids.Round_Widget_id.add_widget(RoundWidget(size_hint_y=0.5, pos_hint={'top': 1}))

    def del_rounds(self):
        print(self.ids.Round_Widget_id.children)
        self.ids.Round_Widget_id.remove_widget(self.ids.Round_Widget_id.children[-1])

        # self.ids.Box_rounds.remove_widget(self.ids.test)

    def dialog_dismiss(self):
        self.dialog_dismiss()


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
