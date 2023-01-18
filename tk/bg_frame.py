'''
Author: Elidas
Email: pyro.elidas@gmail.com
Python version: 3.9
Date: 2021-08-24
'''

#__DEPENDENCIES__#
from tkinter import *

from Background import Background

#__AUXILIARS__#
root = Tk()
root.geometry('200x100')
#root.config(bg='grey')
main = Frame(root)
main.pack(fill='both', expand=1)
bg = Background(main, 'imgs/test.png')#, row=0, column=0)
bg.pack(fill='both', expand=1)
#bg.resizeEqualToWidth(500)
#root.wm_attributes('-transparentcolor', 'grey')
l1 = Label(bg, text='Hola Mundo', fg='black').grid(row=0, column=0)
#Background(l1, 'imgs/test.png')
root.mainloop()

#__MAIN CODE__#
