from prettytable import PrettyTable

# Ejemplo de uso de un paquete instalable.

tabla = PrettyTable(["Pokemon name", "Type"])  # Creamos una tabla con dos columnas.
tabla.add_row(["Pikachu", "Electric"])  # Añadimos las filas
tabla.add_row(["Squirtle", "Water"])
tabla.add_row(["Charmander", "Fire"])
print(tabla)

print()
# Otra manera

tabla2 = PrettyTable()
tabla2.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
tabla2.add_column("Type", ["Electric", "Water", "Fire"])


# Podemos cambiar el formato de nuestra tabla modificando los atributos de la clase.
tabla2.align = "l"

print(tabla2)
