from tkinter import *
from tkinter import messagebox
from time import sleep
import threading as th
import datetime, json, os

class Pomodoros(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # Attributes
        self.master = master
        self.thread = th.Thread(target=self.pomodoro, daemon=True)
        self.pause = False
        self.minutes: int
        self.pom:tuple
        self.color:str
        self.period:str
        
        self.load_config()
        
        # Main Widgets
        self.time_babel = Label(self, text='Tiempo de estudio: ')
        self.time_babel.grid(row=1, column=0)
        
        self.study = Entry(self, width=5, justify=RIGHT)
        self.study.grid(row=1, column=1)
        
        self.set_button = Button(self, text='Set', command=self.set_time)
        self.set_button.grid(row=1, column=2, padx=5)
        
        self.period_counter = Label(self, text='Pomodoro numero _ de _', font=('Consolas', 12))
        self.period_counter.grid(row=2, columnspan=3, padx=5)
        
        self.loop_counter = Label(self, text='loop _ de 4', font=('Consolas',10))
        self.loop_counter.grid(row=3, columnspan=3)
        
        self.clock = Label(self, text='00:00', font=('Consolas', 20), background='light green')
        self.clock.grid(row=4, columnspan=3)
        
        self.current_phase = Label(self, text='Status', font=('Consolas',15), background='light green')
        self.current_phase.grid(row=5, columnspan=3)
        
        self.run_button = Button(self, text='Inicio', state=DISABLED, command=self.thread.start)
        self.run_button.grid(row=6, column=0, columnspan=3, sticky=W, padx=10)
        
        self.pause_button = Button(self, text='Pausa', command=self.pausa, state=DISABLED)
        self.pause_button.grid(row=6, column=0, columnspan=3, sticky=N, padx=5)
        
        self.reboot_btn = Button(self, text='Reinic', command=self.reboot, state=DISABLED)
        self.reboot_btn.grid(row=6, column=0, columnspan=3, sticky=E, padx=10)
    
    def set_time(self):
        t = self.calc_min()
        loop = (self.focus + self.rest) * 3 + (self.focus + self.rest_L)
        if t != 0:
            self.n_loop = (t//loop)
            if t % loop:
                self.n_loop += 1
        self.period_counter.config(text=f'Pomodoro numero 0 de {self.n_loop}')
        self.study.config(state=DISABLED)
        self.set_button.config(state=DISABLED)
        self.run_button.config(state=NORMAL)
        self.pause_button.config(state=NORMAL)
        self.reboot_btn.config(state=NORMAL)
    
    def pausa(self):
        if self.pause:
            self.pause = False
            self.pause_button.config(text='Pausa')
        else:
            self.pause = True
            self.pause_button.config(text='Continuar')
    
    def set_bg(self, color):
        self.master.config(background=color)
        self.config(background=color)
        self.time_babel.config(background=color)
        self.period_counter.config(background=color)
        self.loop_counter.config(background=color)
        self.current_phase.config(background=color)
        self.clock.config(background=color)
    
    def timer(self, minutes:int, pom:tuple, color:str, period:str):
        f = minutes*60
        self.set_bg(color)
        self.period_counter.config(text=f'Pomodoro {pom[0]} de {pom[1]}')
        self.current_phase.config(text=period)
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
            messagebox.showwarning(title='Cambio de fase', message='La fase de concentración he finalizado\nEmpieza fase de des conexión')
            if loop%4 != 0:
                self.timer(self.rest, (i, self.n_loop), 'light blue', 'Des conexión')
                messagebox.showwarning(title='Cambio de fase', message='La fase de relax he finalizado\nEmpieza fase de concentración.')
                loop += 1
            else:
                self.timer(self.rest_L, (i, self.n_loop), 'light green', 'Des conexión Larga')
                messagebox.showwarning(title='Cambio de fase', message='La fase de relax he finalizado\nEmpieza fase de concentración.')
                i += 1
                loop = 1
        self.reboot_btn.config(state=DISABLED)
        self.run_button.config(text='Reset', command=self.reboot)
    
    def reboot(self):
        # variables
        del self.thread
        self.thread = th.Thread(target=self.pomodoro, daemon=True)
        self.n_loop = int()
        #TODO: Falta reiniciar todo el objeto
        # Texto
        self.period_counter.config(text=f'Pomodoro _ de _')
        self.loop_counter.config(text=f'Loop _ de 4')
        self.clock.config(text='00:00')
        self.current_phase.config(text='STANDBY')
        # Botones
        self.study.config(state=NORMAL)
        self.set_button.config(state=NORMAL)
        self.run_button.config(state=DISABLED)
        self.pause_button.config(state=DISABLED)
        self.reboot_btn.config(state=DISABLED)
    
    def calc_min(self):
        h0 = int(datetime.datetime.now().strftime('%H'))
        m0 = int(datetime.datetime.now().strftime('%M'))
        if ':' in self.study.get():
            hf = int(self.study.get().split(':')[0])
            mf = int(self.study.get().split(':')[-1])
            return (hf-h0)*60 + (mf-m0)
        else:
            return int(self.study.get())
    
    def load_config(self):
        path = '/'.join(os.path.realpath(__file__).split('\\')[:-1])
        conf = json.load(open(os.path.join(path,'files/config.json'), 'r'))
        self.focus = conf['focus']
        self.rest = conf['rest']
        self.rest_L = conf['rest']*self.rest