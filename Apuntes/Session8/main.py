import csv
import pandas


# De esta manera creamos la lista con las filas, pero habría que retocar mucho
with open("./weather_data.csv") as tiempo:
    lista_tiempo = tiempo.readlines()
    print(lista_tiempo)
    print()

# Usaremos la libreria de csv para leer el archivo y pasarlo como una lista
with open("./weather_data.csv") as tiempo:
    lista_tiempo = csv.reader(tiempo)
    temperaturas = []
    for fila in lista_tiempo:  # Sacamos el campo de temperatura y lo metemos en una lista convertido en número
        if fila[1].isdigit():
            grados = int(fila[1])
            temperaturas.append(grados)
    print(temperaturas)


# Otra manera es trabajando con la libreria pandas
datos = pandas.read_csv("weather_data.csv")  # No hace falta usar el método open y el formato de salida es mejor.
print(datos)
print()
print(datos["temp"])  # Imprimimos solo la columna de temperaturas. Mucho más fácil que el código anterior

