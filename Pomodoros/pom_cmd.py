from tkinter import *
from tkinter import messagebox
from time import sleep
import threading as th
import os

def timer(minutes:int, pom:tuple, color:str, period:str):
    f = 0
    os.system('color 7')
    input(f'[i] Iniciando periodo de {period.upper()}')
    os.system(f'color {color}')
    while f < minutes*60:
        os.system('cls')
        print(f'Pomodoro {pom[0]} de {pom[1]}')
        print(f'Periodo de {period.lower()}... {minutes} minutos')
        min = f//60
        if len(str(min)) == 1:
            min = f'0{min}'
        sec = f % 60
        if len(str(sec)) == 1:
            sec = f'0{sec}'
        print(f'\t{min}:{sec}')
        sleep(1)
        f += 1


i = 1
t = int(input('[+] Introduce la duración del TOTAL del tiempo de estudio (en minutos):\n>>> '))
focus = 15  # Color 4
rest = 5  # Color 3
rest_L = 3*rest  # Color B
loop = (focus + rest) * 3 + (focus + rest_L)
if t != 0:
    n_loop = (t//loop)
    if t % loop:
        n_loop += 1
    while i < n_loop:
        timer(focus, (i, n_loop), '4', 'CONCENTRACIÓN')
        if i % 4 != 0:
            timer(rest, (i, n_loop), '3', 'Desconexión')
        else:
            timer(rest_L, (i, n_loop), 'B', 'Desconexión Larga')
            i += 1
else:
    while True:
        try:
            timer(focus, (i, '...'), '4', 'CONCENTRACIÓN')
            if i % 4 != 0:
                timer(rest, (i, '...'), '3', 'Desconexión')
            else:
                timer(rest_L, (i, '...'), 'B', 'Desconexión')
                i += 1
        except KeyboardInterrupt:
            break
