'''
Author: Elidas
Email: pyro.elidas@gmail.com
Python version: 3.9
Date: 2021-08-24
'''

#__LIBRARIES__#
from tkinter import *

#__MAIN CLASS__#
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
        self.config(font = kwargs['font'])
        self.config(offvalue=False, onvalue=True)
        self.config(variable = self.__control_var)
        self.bind('<ButtonRelease-1>', self.apply_codependencyes)

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

    def apply_codependencyes(self, event):
        '''
        Applyes the dependencies set.
        If CheckBox, deactivates.
        If Entry
        '''
        self.apply_dependencies()
        for item in self.__dependencies:
            if isinstance(item, Checkbox):
                item.deselect()
                item.apply_dependencies()
    
    def apply_dependencies(self):
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
            obj = (item['text'], item.is_active())
            items.append(obj)
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
    