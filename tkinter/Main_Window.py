'''
Author: python-elidas
Email: pyro.elidas@gmail.com
Python Version: 3.9
Date: 2022-03-13
Version: 0.1.0
'''

#__LIBRARIES__#
from tkinter import *
import simply_sqlite as SQL
from New_User import New_User
from Log_In_Class import Log_In

# __MAIN_WINDOW__ #
class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self._db = SQL('files/generic')
        
        self.iconbitmap()
        self.title()
        self.geometry('100x100')
        
        self._frame = New_User(self)
        self._frame.pack(fill=NONE, expand=1)
        
        self._frameName = str(self._frame)[2:]
        
    def switch_frames(self, frame):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame(self)
        self._frame.pack(fill=NONE, expand=1)
        
    def save_new_user(self):
        pass # TODO
        
    def load_db(self): # TODO
        pass
    

#__MAIN RUN__#
if __name__ == '__main__':
    window = Window()
    window.mainloop()