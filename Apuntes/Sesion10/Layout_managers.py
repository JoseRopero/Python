from tkinter import *

# Pack() empaqueta cada uno de los widgets junto a otros en un formato vagamente lógico.
# Por defecto empezará por la parte superior y empaquetará justo debajo.

# Place() posicionamiento preciso. Valores x, y


def button_clicked():
    print("Vaya, han dado click")
    my_label.config(text="Han hecho click, me han cambiado.")
    my_label.config(text=entrada.get())


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)  # Definimos el tamaño minimo de la ventana.

# Label
my_label = Label(text="Soy una etiqueta", font=("Arial", 24, "italic"))
my_label.place(x=0, y=0)

# Button
button = Button(text="Click", command=button_clicked)  # Cuando detecta un evento (click), llamará a la función.
button.pack()

# Entry
entrada = Entry(width=30)
entrada.insert(END, string="Escribe algo")  # Para tener un texto al iniciar la ventana
entrada.pack()

window.mainloop()  # Para mantener la ventana abierta
