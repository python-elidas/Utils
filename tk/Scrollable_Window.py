'''
Author: Elidas
Email: pyro.elidas@gmail.com
Python version: 3.9
Date: 2021-08-24
'''

#__LIBRARIES__#
from tkinter import *

#__Main Class__#
class ScrollWindow(Canvas):
    '''
    A simplified way to create a scrollable window
    '''
    def __init__(self, master):
        Canvas.__init__(self, master)
                
        #Creamos lo necesario
        self.frame = Frame(self)
        self.vbar = Scrollbar(self.master, orient=VERTICAL, command=self.yview)
        
        #Configuramos
        self.config(yscrollcommand=self.vbar.set)
        self.frame.bind('<Configure>', self.__updateScrollRegion)
        self.bind_all('<MouseWheel>', self.__on_mousewheel)
        self.vbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.create_window(0, 0, window=self.frame, anchor=NW)
        
    def __updateScrollRegion(self, event):
        print('true')
        self.update_idletasks()
        self.config(scrollregion=self.frame.bbox())
        
    def __on_mousewheel(self, event):
        self.yview_scroll(-1*int(event.delta/120), "units")
    
    def update(self):
        self.__updateScrollRegion(None)
        
#__usage Example__#
if __name__ == "__main__":
    from Add_Delete_Buttons import Add_Delete

    # root creation and configuration
    root = Tk() 
    root.geometry('275x100')

    #creation of the scrollable frame
    scrl_frm = ScrollWindow(root)
    scrl_frm.pack(fill=NONE, expand=1)

    #Adding some items
    Label(scrl_frm, text='Hola Mundo').grid(row=0, column=0)
    name = Entry(scrl_frm)
    name.grid(row=0, column=1)

    #buttons to add or delete rows of copied items
    Add_Delete(scrl_frm, max_row=15) #configured to copy the row only 4 times, 5 rows in total count

    

    root.mainloop()