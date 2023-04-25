'''
Author: Elidas
Email: pyro.elidas@gmail.com
Python version: 3.9
Date: 2021-08-24
'''

#__LIBRARIES__#
from tkinter import *

#__Main Class__#
class Add_Delete(Button):
    '''
    Creates a button pair to add or delete a copy of the row
    in which they are placed.
    ONLY WITH GRID!!
    '''
    def __init__(self, master, scale=1, min_row=1, max_row=-1, textFont='Bell MT', textSize=10):
        Button.__init__(self, master)
        self.__min = min_row
        self.__max = max_row
        self.__row = self.master.grid_size()[1]
        self.__dic = self.master.__dict__['children'].values()
        self.add = Button(
            master, text='+',
            font=(textFont, int(textSize*scale)),
            command=self.__add_row
        )
        self.add.grid(row=master.grid_size()[1]-1, column=master.grid_size()[0], padx=10)
        self.delete = Button(
            master, text='-',
            font=(textFont, int((textSize)*scale)),
            state=DISABLED, width=self.add['width'],
            command=self.__del_row
        )
        self.delete.grid(row=master.grid_size()[1]-1, column=master.grid_size()[0]+1)
        
    def __copiable(self, item):
        no_copy = [Button, Frame]
        for type in no_copy:
            if isinstance(item, type):
                return False
        return True
            
    def __add_row(self):
        '''
        Adds a new row with the same items in the row below
        '''
        to_copy = [i for i in self.__dic if self.__copiable(i) and i.grid_info()['row']==self.__row-1]
        for item in to_copy:
            new = type(item)(self.master)
            for key in list(item.keys())[:-1]:
                try:
                    new.config({key: item[key]})
                    try:
                        new.current(0)
                    except:
                        pass
                except Exception:
                    pass
            for info in list(item.grid_info()):
                try:
                    new.grid({info: item.grid_info()[info]})
                    new.grid(row=self.__row)
                except:
                    pass
        self.add.grid(row=self.__row)
        self.delete.grid(row=self.__row)
        self.__row = self.master.grid_size()[1]
        if self.__row >= self.__min:
            self.delete.config(state=NORMAL)
        if self.__row == self.__max and self.__max != -1:
            self.add.config(state=DISABLED)
        
    def __del_row(self):
        '''
        Deletes the current row of items.
        '''
        to_delete = [i for i in self.__dic if not isinstance(i, Button) and i.grid_info()['row']==self.__row-1]
        for item in to_delete:
            item.destroy()
        self.add.grid(row=self.__row-2)
        self.delete.grid(row=self.__row-2)
        self.__row = self.master.grid_size()[1]
        if self.__row <= self.__min:
            self.delete.config(state=DISABLED)
        if self.__row < self.__max:
            self.add.config(state=NORMAL)
            
            
#__usage example__#
if __name__=='__main__':
    root = Tk() # root creation
    root.geometry('250x200') # geometry of the window
    
    #items to be copied
    Label(root, text='Hola Mundo').grid(row=0, column=0)
    name = Entry(root)
    name.grid(row=0, column=1)
    
    #buttons to add or delete rows of copied items
    Add_Delete(root, max_row=5) #configured to copy the row only 4 times, 5 rows in total count
    
    #mainloop
    root.mainloop()