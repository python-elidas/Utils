(es)

Descripción General:

    Ampliación del paquete TkInter con herramientas desarrolladas por necesidad de diferentes proyectos.

Contenido

>>> Add Delete Buttons (Add_Delete):

    Se trata de im pr de botones [+] [-] que copian o eliminan los elementos Tk de la fila en la que se encuentran.

>>> Parámetros de entrada:

    min_row -> Por definición establecido en 1, establece el mínimo de filas que deben permanecer

    max_row -> Establece el máximo de copias as realzar, por definición establecido en -1, lo que indica que no hay límite de copias.

>>> Ejemplo de uso:

    if __name__=='__main__':
    root = Tk() # root creation
    root.geometry('275x200') # geometry of the window
    
    # items to be copied
    Label(root, text='Hola Mundo').grid(row=0, column=0)
    name = Entry(root)
    name.grid(row=0, column=1)

    # buttons to add or delete rows of copied items
    copy_buttons = Add_Delete(root, max_row=5) # configured to copy the row only 4 times, 5 rows in total count
    
    auto_move = Label(root, text='Este texto se mueve solo!')
    auto_move.grid(row=1, column=1)
    
    copy_buttons.add_extra(auto_move)
    
    # mainloop
    root.mainloop()





>>> Control de versiones:

- 0.12.0:   Primera version estable.
- 0.13.0:   Añadido en ScrollableWindow el método collect_children
- 0.14.0:   Añadida opción de añadir otros elementos a los botones Add_Delete fuera de la linea
            a copiar.
