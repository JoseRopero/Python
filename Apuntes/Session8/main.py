import csv
import statistics

import pandas


# De esta manera creamos la lista con las filas, pero habría que retocar mucho
print("Método normal para leer fichero:\n")
with open("./weather_data.csv") as tiempo:
    lista_tiempo = tiempo.readlines()
    print(lista_tiempo)
    print()

# Usaremos la libreria de csv para leer el archivo y pasarlo como una lista
print("Método usando la clase csv:\n")
with open("./weather_data.csv") as tiempo:
    lista_tiempo = csv.reader(tiempo)
    temperaturas = []
    for fila in lista_tiempo:  # Sacamos el campo de temperatura y lo metemos en una lista convertido en número
        if fila[1].isdigit():
            grados = int(fila[1])
            temperaturas.append(grados)
    print(temperaturas)
    print()


# Otra manera es trabajando con la libreria pandas
print("Usando libreria pandas:\n")
datos = pandas.read_csv("weather_data.csv")  # No hace falta usar el método open y el formato de salida es mejor.
print(datos)
print()
print(datos["temp"])  # Imprimimos solo la columna de temperaturas. Mucho más fácil que el código anterior
print()

# Método para pasar los datos a diccionario en pandas:
print("Pasar a diccionario los datos")
datos_dic = datos.to_dict()
print(datos_dic)
print()
print("Pasamos la lista de temperaturas a una list de Python")
datos_list = datos["temp"].to_list()
print(datos_list)
print()

# Calculamos la media de las temperaturas
print(round(sum(datos_list)/len(datos_list), 2))  # Métodos de list
print(round(statistics.mean(datos_list), 2))  # Métodos de statistics
print(round(datos["temp"].mean(), 2))  # Métodos de panda
print(datos["temp"].max())  # Imprime el máximo de la columna.

# Otra forma de mostrar la columna es utilizando la variable. Panda convierte el nombre de la columna en una variable.
print(datos.temp)
print()

# Para sacar los datos de una fila:
print(datos[datos.day == "Monday"])
print()
# Sacamos la fila con la temperatura maxima.
print(datos[datos.temp == datos.temp.max()])
