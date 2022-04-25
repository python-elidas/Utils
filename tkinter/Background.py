'''
Author: Elidas
Email: pyro.elidas@gmail.com
Python version: 3.9
Date: 2021-08-24
'''

#__MODULES TO BE INSTALLED__#
#? Pillow: pip install Pillow

#__LIBRARIES__#
from tkinter import *
from PIL import Image, ImageTk

#__Main Class__#
class Background(Label):
    '''
    A class to simplify adding backgrounds .
    '''
    def __init__(self, master, img, **kwargs):
        Label.__init__(self, master)
        self._pic = Image.open(img)
        bg = ImageTk.PhotoImage(self._pic)
        self.config(image=bg)
        self._img = bg
        self.update()
        self.size = (self.winfo_reqwidth(), self.winfo_reqheight())
        self.width = self.winfo_reqwidth()
        self.height = self.winfo_reqheight()
        if 'x' in list(kwargs.keys()) or 'y' in list(kwargs.keys()):
            for key in list(kwargs.keys()):
                self.place({key : kwargs[key]})
        elif 'row' in list(kwargs.keys()) or 'column' in list(kwargs.keys()):
            for key in list(kwargs.keys()):
                self.grid({key : kwargs[key]})
    
    def centerItemX(self, item, y):
        '''
        Centers an item horizontally
        '''
        item.update()
        x = (self.size[0] - item.winfo_reqwidth()) / 2
        item.place(x=x, y=y)
    
    def centerItemY(self, item, x):
        '''
        centers an item vertically
        '''
        item.update()
        y = (self.size[1] - item.winfo_reqheight()) / 2
        item.place(x=x, y=y)
    
    def resizeXY(self, x, y):
        '''
        Resizes the background with given height and width
        '''
        x, y = int(x), int(y)
        bg = ImageTk.PhotoImage(
            self._pic.resize((x, y))
        )
        self.config(image=bg)
        self.img = bg
        self.update()
        self.size = (self.winfo_reqwidth(), self.winfo_reqheight())
        
    def resizePerc(self, perc):
        '''
        Resizes the background to a given percentage of the original sizes
        '''
        x = int(self._pic.size[0] * perc)
        y = int(self._pic.size[1] * perc)
        bg = ImageTk.PhotoImage(
            self._pic.resize((x, y))
        )
        self.config(image=bg)
        self.img = bg
        self.update()
        self.size = (self.winfo_reqwidth(), self.winfo_reqheight())
    
    def resizeEqualToWidth(self, width):
        '''
        Resizes the background to a certain width preserving the heigh-width
        ratio
        '''
        x = int(width)
        y = int(self._pic.size[1] * (width / self._pic.size[0]))
        bg = ImageTk.PhotoImage(
            self._pic.resize((x, y))
        )
        self.config(image=bg)
        self.img = bg
        self.update()
        self.size = (self.winfo_reqwidth(), self.winfo_reqheight())