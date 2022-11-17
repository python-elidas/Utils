# -*- coding: utf-8 -*-
#__LIBRARIES__
import New_User
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import hashlib as hash

#__MAIN WINDOW__#
class main_window(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title('NEW USER')
        self.geometry('400x120')
        
        self._frame = Log_In(self)
        self._frame.pack(fill=NONE, expand=1)

#__LOG IN__#
class Log_In(Frame):
	def __init__(self, master):
		Frame.__init__(self)
		
		self._master = master

		#WINDOW CONFIG#
		self._master.geometry('400x120')
		self._master.resizable(FALSE, FALSE)
		# TODO self._master.iconbitmap()

		#MAIN WINDOW#
		#? If log in with User not with name
		#Label(self, text = 'Usuario: ').grid(row = 2, column = 0, sticky = W, padx = 10, pady = 5)
		#self.user = Entry(self, width = 35)
		#self.user.grid(row = 2, column = 1, columnspan = 1, sticky = W)
		#self.user.focus()

		#? If log in with name
		Label(self, text = 'Nombre: ').grid(row = 2, column = 0, sticky = W, padx = 10, pady = 5)
		self.user = Entry(self, width = 35)
		self.user.grid(row = 2, column = 1, columnspan = 1, sticky = W)
		self.user.focus()

		Label(self, text = 'Apellido: ').grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
		self.surname = Entry(self, width = 35)
		self.surname.grid(row = 3, column = 1, columnspan = 1, sticky = W)

		Label(self, text = 'Contraseña: ').grid(row = 4, column = 0, sticky = W, padx = 10, pady = 3)
		self.pasword = Entry(self, width = 35)
		self.pasword.grid(row = 4, column = 1,  columnspan = 1, sticky = W)
		self.pasword.bind('<Key>', self.t_s)#mustra el caracter introducido 1s
		self.pasword.bind('<Return>', self.log)

		self.see = Button(self, text = 'Mostrar')
		self.see.bind('<ButtonPress>', self.show_password)#muestra la contaseña en ambos campos al pulsar
		self.see.bind('<ButtonRelease>', self.hide_password)#oculta la contraseña en ambos campos al soltar
		self.see.grid(row = 4, column = 2, padx = 3)

		self.log_btn = Button(self, text = 'Iniciar Sesión', command = self.log_in)
		self.log_btn.grid(row = 5, column = 1, sticky = E, pady = 3)

		self.new_btn = Button(self, text = 'Nuevo Usuario', command = self.new_user)
		self.new_btn.grid(row = 5, column = 1, sticky = W, pady = 3)

	def new_user(self):#Accede a la ventana de creación de ususarios
		self._master.switch_frames(New_User)

	def show_password(self, event):# muestra los caracteres originales de la contraseña.
		self.pasword.config(show = '')

	def hide_password(self, event):# Muestra el caracter '.' en vez de el introducido en el campo.
		self.pasword.config(show = '·')

	def t_s(self, event):
		self.pasword.config(show = '')
		#Hide text after 750 milliseconds
		self.pasword.after(750, lambda: self.pasword.config(show = '·'))

	def log_in(self):
		hash_pass = self.gen_hash()
		users = self._master._users
		for user in users:
			if users[user]['password'] == hash_pass:
				return True
		else:
			messagebox.showerror(title='Información no valida.', message='Verifique los datos introducidos y vuelva a intentarlo.')
			return False
	
	def log(self, event):
		self.log_in()
 
	def gen_hash(self):
		model = hash.new('sha256')
		model.update(self.pasword.get().encode('utf-8'))
		return model.hexdigest()
	

def run():
	itc = Log_In()
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
