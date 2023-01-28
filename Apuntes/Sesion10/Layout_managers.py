from tkinter import *

# Pack() empaqueta cada uno de los widgets junto a otros en un formato vagamente lógico.
# Por defecto empezará por la parte superior y empaquetará justo debajo.

# Place() posicionamiento preciso. Valores x, y. Al ser tan preciso puede resultar demasiado complicado si tenemos
# muchos widgets.

# Grid() imagina que tu programa es una cuadrícula (Filas y columnas). Incompatible con Pack().


def button_clicked():
    print("Vaya, han dado click")
    my_label.config(text="Han hecho click, me han cambiado.")
    my_label.config(text=entrada.get())


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)  # Definimos el tamaño minimo de la ventana.
window.config(padx=20, pady=20)  # Para añadir relleno a la ventana.

# Label
my_label = Label(text="Soy una etiqueta", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)
my_label.config(padx=5, pady=5)

# Button
button = Button(text="Click", command=button_clicked)  # Cuando detecta un evento (click), llamará a la función.
button.grid(column=1, row=1)
button.config(padx=5, pady=5)

button2 = Button(text="New button")
button2.grid(column=2, row=0)
button2.config(padx=5, pady=5)

# Entry
entrada = Entry(width=30)
entrada.insert(END, string="Escribe algo")  # Para tener un texto al iniciar la ventana
entrada.grid(column=3, row=2)

window.mainloop()  # Para mantener la ventana abierta
