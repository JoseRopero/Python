from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)  # Definimos el tamaño minimo de la ventana.

# Label
my_label = Label(text="Soy una etiqueta", font=("Arial", 24, "italic"))
my_label.pack()  # Para que se pueda mostrar en la ventana

# Para configurar o actualizar un elemento ya creado tenemos varias opciones:
my_label["text"] = "Nuevo texto"
my_label.config(text="Hola de nuevo")


# Button
def button_clicked():
    print("Vaya, han dado click")


def actualizar_label():
    my_label.config(text="Han hecho click, me han cambiado.")


def actualizar_label_entrada():
    my_label.config(text=entrada.get())


button = Button(text="Click", command=button_clicked)  # Cuando detecta un evento (click), llamará a la función.
button.pack()

button2 = Button(text="Cambiar texto etiqueta", command=actualizar_label)
button2.pack()

# Entry
entrada = Entry(width=30)
entrada.insert(END, string="Escribe algo")  # Para tener un texto al iniciar la ventana
entrada.pack()
print(entrada.get())
button3 = Button(text="Click para introducir label", command=actualizar_label_entrada)
button3.pack()

# Text
texto = Text(height=5, width=30)
texto.focus()  # Aparece el cursor al abrir la ventana.
texto.insert(END, "Texto multi-linea")
print(texto.get("1.0", END))  # Imprime desde la línea 1 caracter 0.
texto.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())  # Cada vez que le damos al spinbox imprime por pantalla


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())  # Imprime 1 cuando se marca, 0 cuando se quita.


checked_state = IntVar()  # Le asignamos una variable para los numeros a imprimir (1, 0)
checkbutton = Checkbutton(text="Encendido?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Opción 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Opción 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()  # Para mantener la ventana abierta
