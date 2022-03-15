'''
Author: python-elidas
Email: pyro.elidas@gmail.com
Python Version: 3.9
Date: 2022-03-13
Version: 0.1.0
'''

#__LIBRARIES__#
from tkinter import *
import simply_sqlite as sSQL
from New_User import New_User
from Log_In_Class import Log_In

# __MAIN_WINDOW__ #
class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self._db = sSQL.SQL('generic')
        
        try:
            self.load_users()
        except Exception:
            self._users = dict()
        
        self.iconbitmap()
        self.title()
        self.geometry('100x100')
        
        self.firstFrame()
        self._frame.pack(fill=NONE, expand=1)
        
        self._frameName = str(self._frame)[2:]
    
    def firstFrame(self):
        if not len(self._users):
            self._frame = New_User(self)
        else:
            self._frame = Log_In(self)
        
    def switch_frames(self, frame):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame(self)
        self._frame.pack(fill=NONE, expand=1)
             
    def save_new_user(self, user):
        if not 'users' in self._db.find_tables():
            self._db.create_table('users', 'id_code', 'TEXT')
            for column in list(user.keys())[1:]:
                self._db.insert_column('users', column, 'TEXT')
        self._db.insert_info('users', 'id_code', user['id_code'])            
        code = user['id_code']
        for column in list(user.keys())[1:]:
            self._db.update('users', column, 'id_code', (user[column], code))
        self.load_users()
        
    def load_users(self):
        self._users = dict()
        info = ['name', 'surname', 'user', 'mail', 'password']
        for user in self._db.get_all_rows('users'):
            d = dict()
            n = 1
            for i in range(5):
                d[info[i]] = user[n+i]
            self._users[user[0]] = d

#__MAIN RUN__#
if __name__ == '__main__':
    window = Window()
    window.mainloop()