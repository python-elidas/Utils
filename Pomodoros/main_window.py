from tkinter import *
import os
from Pomodoro_frme import Pomodoros

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        # Configure
        self.title('Pyro Pom')
        self.geometry('225x175')
        self.resizable(0, 0)
        try:
            path = '/'.join(os.path.realpath(__file__).split('\\')[:-1])
            self.iconbitmap(os.path.join(path,'files/D20_2.ico'))
        except:
            pass
        
        self._frame = Pomodoros(self)
        self._frame.pack(fill=NONE, expand=1)
        
        
if __name__ == '__main__':
    p = Main()
    p.mainloop()