import os
from tkinter import *
from tkinter import filedialog


def change_name(new, coinc, root=None):
    if not root:
        root = Tk()
        file = filedialog.askdirectory(title='Seleccione carpeta root')
        root.destroy()
        root = '/'.join(str(file).split('/'))
        for folder in os.listdir(root):
            print(folder)
            dir = os.path.join(root, folder)
            if coinc in str(folder):
                #print(dir, type(folder))
                os.rename(str(folder), new)
            else:
                change_name(new, coinc, dir)
        return True
    else:
        for folder in os.listdir(root):
            
            if coinc in str(folder):
                #print(dir, type(folder))
                os.rename(os.path.join(root, folder), os.path.join(root, new))
            else:
                try:
                    dir = os.path.join(root, folder)
                    change_name(new, coinc, dir)
                except:
                    pass
        return True
    
if __name__ == '__main__':
    coinc = input('Establezca patron de búsqueda:\n>>> ')
    new = input('Establezca nuevo nombre:\n>>> ')
    change_name(new, coinc)