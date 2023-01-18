# -*- coding: utf-8 -*-
#__LIBRARIES__
from Log_In_Class import Log_In
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import hashlib as hash
import string

#__MAIN WINDOW__#
class main_window(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title('NEW USER')
        self.geometry('575x150')
        
        self._frame = New_User(self)
        self._frame.pack(fill=NONE, expand=1)

#__CREATE NEW USER FRAME__#
class New_User(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self._master = master
        self._master.geometry('575x150')
        self._master.resizable(FALSE, FALSE)
        # TODO self._master.iconbitmap()
        
        # widgets
        Label(self, text = '*Nombre:').grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
        self.name = Entry(self, width = 25)
        self.name.grid(row = 0, column = 1, sticky = W)
        self.name.focus()
        
        Label(self, text = '*Apellido:').grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)
        self.surname = Entry(self, width = 30)
        self.surname.grid(row = 0, column = 3, sticky = W)
        
        Label(self, text = '*Usuario:').grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
        self.user = Entry(self, width = 25)
        self.user.grid(row = 1, column = 1, sticky = W)
        
        Label(self, text = '*Email:').grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)
        self.mail = Entry(self, width = 30)
        self.mail.grid(row = 1, column = 3, sticky = W)
        self.mail.bind('<FocusOut>', self.verify_mail)
        
        Label(self, text = '*Contraseña:').grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)
        self.password = Entry(self, width = 25, show = '*')
        self.password.bind('<Key>', self.t_s)#mustra el caracter introducido 1s
        self.password.grid(row = 2, column = 1, sticky = W)
        
        Label(self, text = 'Repita contraseña:').grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)
        self.password2 = Entry(self, width = 25, show = '*')
        self.password2.bind('<Key>', self.t_s2)#mustra el caracter introducido 1s
        self.password2.grid(row = 3, column = 1, sticky = W)
        
        self.see = Button(self, text = 'Mostrar')
        self.see.bind('<ButtonPress>', self.show_password)#muestra la contaseña en ambos campos al pulsar
        self.see.bind('<ButtonRelease>', self.hide_password)#oculta la contraseña en ambos campos al soltar
        self.see.grid(row = 2, column = 2)
        
        self.sumbit = Button(self, text = 'Crear Usuario', command = self.collect)
        self.sumbit.grid(row = 4, column = 1, sticky = E )
        self.back = Button(self, text = 'Atras', command = self.back)
        self.back.grid(row = 4, column = 2, padx = 10, sticky = W)
        
    def show_password(self, event):
        self.password.config(show = '')
        self.password2.config(show = '')
        
    def hide_password(self, event):
        self.password.config(show = '*')
        self.password2.config(show = '*')
        
    def t_s(self, event):
        #print(`event.char`, event.keycode, event.keysym )
        self.password.config(show = '')
        #Hide text after 750 milliseconds
        self.password.after(750, lambda: self.password.config(show = '*'))
        
    def t_s2(self, event):
        #print(`event.char`, event.keycode, event.keysym )
        self.password2.config(show = '')
        # Hide text after 750 milliseconds
        self.password2.after(750, lambda: self.password2.config(show = '*'))
        
    def collect(self):
        attributes = self.__dict__
        user = dict()
        user['id_code'] = self.gen_code()
        if self.verify_password():
            for item in attributes:
                if type(attributes[item]) is Entry and self.verify_box(item):
                    if item == 'password':
                        user[item] = self.encode_password(attributes[item].get())
                    elif not item == 'password2':
                        user[item] = attributes[item].get()
            self._master.save_new_user(user)
            self._master.switch_frames(Log_In)
    
    def gen_code(self):
        string = self.name.get() + \
                 self.surname.get() + \
                 self.user.get()
        model = hash.new('sha256')
        model.update(string.encode('utf-8'))
        return model.hexdigest()[::2]
    
    def encode_password(self, password):
        model = hash.new('sha256')
        model.update(password.encode('utf-8'))
        return model.hexdigest()
    
    def verify_mail(self, event):
        domains = ['hotmail', 'gmail', 'yahoo', 'outlook', 'aol']
        exts = ['com', 'es', 'net']
        mail = self.mail.get()
        domain = mail.split('@')[-1].split('.')[0]
        ext = mail.split('.')[-1]
        if domain in domains and ext in exts:
            self.mail_ok = True
        else:
            messagebox.showerror(title='El correo no es valido', message='Verifique el correo y vuelva a intentarlo.')
        
    def verify_password(self):
        low, up, sym = 0, 0, 0
        symbols = str()
        for i in string.printable:
            if i not in string.ascii_letters:
                symbols += i
        if not self.password.get() == '' or not self.password2.get() == '':
            if self.password.get() == self.password2.get():
                pss = self.password.get()
                for char in pss:
                    if char in string.ascii_uppercase:
                        up += 1
                    elif char in string.ascii_lowercase:
                        low += 1
                    elif char in symbols:
                        sym += 1
            if low > 0 and up > 0 and sym > 0 and len(pss) > 6:
                return True
            else:
                messagebox.showerror('No son validas', 'Debe contener una Mayúscula, una minúscula y un numero o simbolo como mínimo.')
                return False
        else:
            messagebox.showerror('Las Contraseñas no coinciden', 'Verifique los campos de Contraseña')
            return False
        
    def verify_box(self, elem):
        if self.__dict__[elem].get() == '':
            messagebox.showerror('Falta Información', f'El campo {elem} es Obligatorio.')
            return False
        else:
            return True
        
    def back(self):
        self._master.switch_frames(Log_In)

def run():
	itc = main_window()
	itc.mainloop()

if __name__ == '__main__':
	run()

#__BIBLIOGRAPHY__#
'''
	StackOverflow	https://stackoverflow.com
	EffBot.Org		https://effbot.org/tkinterbook/
	Like Geeks		https://likegeeks.com/es/python-es/
	RecursosPython	https://recursospython.com
	Real Python		https://realpython.com/openpyxl-excel-spreadsheets-python/
	W3Schools		https://www.w3schools.com/python/
	ZetCode			http://zetcode.com/tkinter/menustoolbars/
'''
