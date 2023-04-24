import os
from tkinter import *
from config import Config
from Pomodoro_frme import Pomodoros

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        # Configure
        self.title('Pyro Pom')
        self.geometry('230x180')
        self.resizable(0, 0)
        try:
            path = '/'.join(os.path.realpath(__file__).split('\\')[:-1])
            self.iconbitmap(os.path.join(path,'files/D20_2.ico'))
        except:
            pass
        
        self.pom = Pomodoros
        self.cnf = Config
        
        self._frame = Pomodoros(self)
        self._frame.pack(fill=NONE, expand=1)
        
    def switch_frames(self, frame):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame(self)
        self._frame.pack(fill=NONE, expand=1)
        
if __name__ == '__main__':
    p = Main()
    p.mainloop()