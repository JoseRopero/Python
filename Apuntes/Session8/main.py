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
print()

# Para sacar solo un dato de la fila podemos almacenar la fila en una variable y después acceder al dato que queramos.
monday = datos[datos.day == "Monday"]
print(monday.condition)

# Pasar la temperatura del lunes de Celsius a Fahrenheit
temp_monday = monday.temp
print(temp_monday * 1.8 + 32)  # Fórmula para pasar a F -> Los grados C * 1.8 y le sumamos 32
print()

# Crear un dataframe desde 0.
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
datos_students = pandas.DataFrame(data_dict)
print(datos_students)
datos_students.to_csv("new_data.csv")
print()

# Ejercicio. Dado el csv del censo de ardillas. Sacar una tabla con el color del pelaje (grey, red, black) y el
# total de ardillas de cada color.

datos_censo_ardillas = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Con len() obtenemos el número de filas
datos_gray = len(datos_censo_ardillas[datos_censo_ardillas["Primary Fur Color"] == "Gray"])
datos_red = len(datos_censo_ardillas[datos_censo_ardillas["Primary Fur Color"] == "Cinnamon"])
datos_black = len(datos_censo_ardillas[datos_censo_ardillas["Primary Fur Color"] == "Black"])
# Creamos un diccionario con los datos
datos_ardillas_dic = {
    "Color_fur": ["Gray", "Red", "Black"],
    "Count": [datos_gray, datos_red, datos_black]
}
datos_ardillas_dataframe = pandas.DataFrame(datos_ardillas_dic)
datos_ardillas_dataframe.to_csv("Count_ardillas.csv")
