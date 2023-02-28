'''
Author: Elidas
Email: pyro.elidas@gmail.com
Python version: 3.9
Date: 2021-08-24
'''

#__LIBRARIES__#
from tkinter import *

#__Main Class__#
class TerminalWindow(Frame):
    '''
    A simplified way to create a scrollable window
    '''
    def __init__(self, master):
        Frame.__init__(self, master)
                
        self._master = master
        self.__width = 40
        #Creamos lo necesario
        self.__terminal = Listbox(
            self, width=self.__width, 
            background='black', fg='light green', 
            font=('Consolas', 10)
        )
        self.__vbar = Scrollbar(self, orient=VERTICAL, command=self.__terminal.yview)
        
        #Configuramos
        self.__terminal.config(yscrollcommand=self.__vbar.set)
        self.__terminal.pack(fill=BOTH, expand=1, side=LEFT)
        self.__vbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.__set_width()
        
    def add(self, place, text):
        self.__terminal.insert(place, text)
    
    def __set_width(self):
        self.__terminal.update()
        if self.__terminal.winfo_reqwidth() >= self.master.winfo_width():
            while self.__terminal.winfo_reqwidth() >= self.master.winfo_width()-20:
                self.__width -= 1
                self.__terminal.config(width=self.__width)
                print(self.__terminal.winfo_reqwidth(), self.master.winfo_width())
        elif self.__terminal.winfo_reqwidth() < self.master.winfo_width():
            while self.__terminal.winfo_reqwidth() <= self.master.winfo_width()-20:
                self.__width += 1
                self.__terminal.config(width=self.__width)
        
        
#__usage Example__#
if __name__ == "__main__":
    # root creation and configuration
    root = Tk() 
    root.geometry('400x250')

    #creation of the Terminal
    terminal = TerminalWindow(root)
    terminal.grid(row=0, column=0)

    #Adding some items
    for i in range(100):
        terminal.add(END, f'[{i}] Hola Mundo estamos probando la clase terminal')
    
    root.mainloop()