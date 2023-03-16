from tkinter import *
from Pomodoro_frme import Pomodoros

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        # Configure
        self.title('Pyro Pom')
        self.geometry('225x175')
        self.resizable(0, 0)
        #self.iconbitmap('D20_2.ico')
        
        self._frame = Pomodoros(self)
        self._frame.pack(fill=NONE, expand=1)
        
        
if __name__ == '__main__':
    p = Main()
    p.mainloop()