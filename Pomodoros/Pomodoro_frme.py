from tkinter import *
from tkinter import messagebox
from time import sleep
import threading as th
import os

class Pomodoros(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # Attributes
        self.thread = th.Thread(target=self.pomodoro, daemon=True)
        self.focus = 25 # Color 4
        self.rest = 5 # Color 3
        self.rest_L = 3*self.rest # Color B
        self.loop = (self.focus + self.rest) * 3 + (self.focus + self.rest_L)
        self.pause = False
        self.minutes: int
        self.pom:tuple
        self.color:str
        self.period:str
        
        # Main Widgets
        Label(self, text='Tiempo de estudio: ').grid(row=1, column=0)
        
        self.study = Entry(self, width=5, justify=RIGHT)
        self.study.grid(row=1, column=1)
        
        self.set_button = Button(self, text='Set', command=self.set_time)
        self.set_button.grid(row=1, column=2, padx=5)
        
        self.period_counter = Label(self, text='Pomodoro numero _ de __', font=('Consolas', 12))
        self.period_counter.grid(row=2, columnspan=3, padx=5)
        
        self.loop_counter = Label(self, text='loop 0 de 4', font=('Consolas',10))
        self.loop_counter.grid(row=3, columnspan=3)
        
        self.clock = Label(self, text='00:00', font=('Consolas', 20), background='light green')
        self.clock.grid(row=4, columnspan=3)
        
        self.current_phase = Label(self, text='Status', font=('Consolas',15), background='light green')
        self.current_phase.grid(row=5, columnspan=3)
        
        self.run_button = Button(self, text='Inicio', state=DISABLED, command=self.thread.start)
        self.run_button.grid(row=6, column=0, sticky=W, padx=10)
        
        self.pause_button = Button(self, text='Pausa', command=self.pausa, state=DISABLED)
        self.pause_button.grid(row=6, column=1, columnspan=2, sticky=E, padx=10)
        
    def set_time(self):
        t = int(self.study.get())
        if t != 0:
            self.n_loop = (t//self.loop)
            if t % self.loop:
                self.n_loop += 1
        self.period_counter.config(text=f'Pomodoro numero 0 de {self.n_loop}')
        self.study.config(state=DISABLED)
        self.set_button.config(state=DISABLED)
        self.run_button.config(state=NORMAL)
        self.pause_button.config(state=NORMAL)
    
    def pausa(self):
        if self.pause:
            self.pause = False
            self.pause_button.config(text='Pausa')
        else:
            self.pause = True
            self.pause_button.config(text='Continuar')
    
    def timer(self, minutes:int, pom:tuple, color:str, period:str):
        f = minutes*60
        self.period_counter.config(text=f'Pomodoro {pom[0]} de {pom[1]}')
        self.current_phase.config(text=period, background=color)
        self.clock.config(background=color)
        while f >= 0:
            min = f//60
            if len(str(min)) == 1:
                min = f'0{min}'
            sec = f%60
            if len(str(sec)) == 1:
                sec = f'0{sec}'
            self.clock.config(text=f'{min}:{sec}')
            sleep(1)
            if not self.pause:
                f-=1
            
    def pomodoro(self):
        i, loop = 1, 1
        while i <= self.n_loop:
            self.loop_counter.config(text=f'Loop {loop} de 4')
            self.timer(self.focus, (i, self.n_loop), 'orange', 'CONCENTRACIÓN')
            messagebox.showwarning(title='Cambio de fase', message='La fase de concentración he finalizado\nEmpieza fase de desconexión')
            if loop%4 != 0:
                self.timer(self.rest, (i, self.n_loop), 'light blue', 'Desconexión')
                messagebox.showwarning(title='Cambio de fase', message='La fase de relax he finalizado\nEmpieza fase de concentración.')
                loop += 1
            else:
                self.timer(self.rest_L, (i, self.n_loop), 'light green', 'Desconexión Larga')
                messagebox.showwarning(title='Cambio de fase', message='La fase de relax he finalizado\nEmpieza fase de concentración.')
                i += 1
                loop = 1
        self.run_button.config(text='Reset', command=self.reboot)
        
    def reboot(self):
        del self.thread
        self.thread = th.Thread(target=self.pomodoro, daemon=True)
        #TODO: Falta reiniciar todo el objeto