'''
Author: Elidas      |   Python Version: 3.9.13
Date: 2021-07-17    |   version: 0.0.1
'''

# __LIBRARIES__ #
import json, os
from tkinter import *

# __MAIN CODE__ #
class Config(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.master = master
        
        Label(self, text='Tiempo de concentración:').grid(row=0, column=0, sticky=W)
        self.focus = Entry(self, width=4)
        self.focus.grid(row=0, column=1, sticky=E)
        
        Label(self, text='Tiempo de Descanso:').grid(row=1, column=0, sticky=W)
        self.rest = Entry(self, width=4)
        self.rest.grid(row=1, column=1, sticky=E)
        self.rest.bind('<KeyRelease>', self.set_long)
        
        Label(self, text='Tiempo largo de concentración:').grid(row=2, column=0, sticky=W)
        self.long = Label(self, text=' x 0 = 00')
        self.long.grid(row=3, columnspan=3, padx=5)
        self.rest_L = Entry(self, width=3, justify=RIGHT)
        self.rest_L.place(x=55, y=66)
        self.rest_L.bind('<KeyRelease>', self.set_long)
        
        self.load_settings()
        
        Button(self, text='Guardar', command=lambda: self.save(self.master)).grid(row=3, columnspan=3, sticky=E)
    
    def set_long(self, event):
        try:
            self.long.config(text=f' x {self.rest.get()} = {int(self.rest.get())*int(self.rest_L.get())}')
        except ValueError:
            pass
    
    def save(self, master):
        path = '/'.join(os.path.realpath(__file__).split('\\')[:-1])
        settings = dict()
        settings['focus'] = int(self.focus.get())
        settings['rest'] = int(self.rest.get())
        settings['long_rest'] = int(self.rest_L.get())
        settings['break'] = 'None'
        json.dump(settings, open(os.path.join(path,'files/config.json'), 'w'))
        master.switch_frames(master.pom)
    
    def load_settings(self):
        path = '/'.join(os.path.realpath(__file__).split('\\')[:-1])
        settings = json.load(open(os.path.join(path,'files/config.json'), 'r'))
        self.focus.insert(END, settings['focus'])
        self.rest.insert(END, settings['rest'])
        self.rest_L.insert(END, settings['long_rest'])
        self.set_long(None)

#__AUXILIARY__#


# __NOTES__ #
'''
'''


# __BIBLIOGRAPHY__ #
'''
'''
