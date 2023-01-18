'''
Author: Elidas
Email: pyro.elidas@gmail.com
Python version: 3.9
Date: 2021-08-24
'''

#__LIBRARIES__#
from tkinter import *

#__MAIN CLASS__#
#__Custom Checkbox__
class Checkbox(Checkbutton):
    '''
    A simplified CheckBox with a simply usage to set active or
    inactive some features.
    '''
    
    def __init__(self, master, **kwargs):
        Checkbutton.__init__(self, master)
        self.__control_var = BooleanVar()
        self.__dependencies = list()
        self.config(text = kwargs['text'])
        try:
            self.config(font = kwargs['font'])
        except:
            pass
        self.config(offvalue=False, onvalue=True)
        self.config(variable = self.__control_var)
        self.bind('<ButtonRelease-1>', self.__bind)
        
        self.binded = [self.apply_codependencyes]
        self.bind('<ButtonRelease-1>', self.__apply_codependencyes)

    def set_text(self, text):
        '''
        Configres only the text shown with the box
        '''
        self.config(text = text)

    def configure(self, **conf):
        '''
        Configures everything that's configurable in a CheckButton
        '''
        for key in list(conf.keys()):
            value = conf[key]
            self.config({key: value})

    def set_dependencies(self, *args):
        '''
        Sets the codependency of this CheckBox with other Checkboxes.
        '''
        for item in args:
            if not isinstance(item, Checkbox) and not isinstance(item, Entry):
                raise TypeError(f'Not supported codependency between Checkbox and {type(item)}')
        else:
            self.__dependencies = list(args)

    def __apply_codependencyes(self, event):
        '''
        Applyes the dependencies set.
        If CheckBox, deactivates.
        If Entry applies changes its state
        '''
        self.__apply_dependencies()
        for item in self.__dependencies:
            if isinstance(item, Checkbox):
                if item.is_active():
                    item.__apply_dependencies()
                item.deselect()
    
    def __apply_dependencies(self):
        '''
        Toggels the state of the entry depending state of the codependent checkbox
        '''
        for item in self.__dependencies:
            if isinstance(item, Entry):
                if item['state'] == NORMAL:
                    item['state'] = DISABLED
                elif item['state'] == DISABLED:
                    item['state'] = NORMAL
                
    def show_dependencies(self):
        '''
        Shows th dependencies between THIS CheckBox and the other CheckBoxes
        '''
        items = list()
        for item in self.__dependencies:
            obj = dict()
            if isinstance(item, Checkbox):
                obj = (item['text'], item.is_active(), item)
            if isinstance(item, Entry):
                obj = ('Entry', item['state'], item)
            items.append(obj)
        items.append((self['text'], self.is_active(), self))
        return items

    def delete_dependencies(self, *args):
        '''
        Deletes the given dependencies
        '''
        for item in args:
            self.__dependencies.remove(item)

    def is_active(self):
        '''
        Returns Either is active or not.
        '''
        return self.__control_var.get()
    
    def add_func_to_bind(self, func):
        '''
        Adds a function to queue to run when the checkbox is clicked.
        functions run every time the checkbox is checked
        '''
        self.binded.append(func)
        
    def __bind(self, event):
        '''
        runs every function in the queue when the checkbox is clicked
        '''
        for func in self.binded:
            func(event)

#__usage example__#
root = Tk()# root creation
Label(root, text='Switch').grid(row=0, column=0)

#creation of dependent check boxes
on=Checkbox(root, text='on')
on.grid(row=1, column=0)
off=Checkbox(root, text='off')
off.grid(row=2, column=0)

#creating a entry dependent on on check box
name = Entry(root)
name.grid(row=1, column=1)
name.insert(0, 'Tu nombre')
name.config(state=DISABLED)

#setting the dependent relations
on.set_dependencies(off, name)
off.set_dependencies(on)

root.mainloop()
