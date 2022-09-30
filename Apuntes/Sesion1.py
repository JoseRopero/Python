#Sesión 1. 

print("Hola mundo\nMi nombre es Jose")  # Con '\n' hacemos un salto de linea.

# Operaciones con str.

cadena = 'hola, Vamos a empezAr con Pythom'
print(type(cadena))  # Con type nos muestra el tipo de variable.
print(cadena.capitalize())  # Con capitalize, la primera letra en mayúsculas y las demás las pasa a minusculas.
print(cadena.title())  # En mayúsculas la primera letra de cada palabra.
print(cadena.lower())  # Todas en minúsculas
print(cadena.upper())  # En mayúsculas.
print(cadena.replace('hola', 'Guay'))  # Reemplaza la palabra.
print(cadena.find('Vamos'))  # Busca una palabra.

listaTexto = cadena.split()  # Pasa la cadena a una lista.
cadena2 = ' '.join(listaTexto)  # Pasa una lista a una cadena con espacios.
cadena3 = '-'.join(listaTexto)  # Entre las comillas podemos poner lo que queramos
print(cadena3)

# Trabajamos con las listas.

lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'x', 'm']  # De esta manera inicializamos una lista.
lista1.remove('c')  # Eliminamos un elemento de la lista.
lista2 = ['g', 'h', 'i', 'j', 'k', 'l']
lista1.append(lista2)  # Añadimos la lista2 a la lista1 (lista anidada).
vacio = []  # Se puede crear una lista vacía.

# Tupla

tupla = ('a', 'b', 'c', 'd', 'e')  # Inicializamos una tupla.

# Diccionario

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # Inicializamos un diccionario.
print(diccionario['a'])  # Imprime el valor de la clave.
resultado = diccionario['a']  # Asignamos el valor a la variable.
diccionario['c'] = 54  # Cambiamos el valor de la clave.
diccionario.pop('d')  # Elimina la clave valor.
del diccionario['a']  # Otra manera de eliminar.

# Conjuntos (set)

a = {1, 2, 3, 4, 5}  # Inicializamos un set (Conjuntos). No se pueden repetir los elementos.
b = {2, 5, 9, 8, 10}
set1 = a | b  # Une los elementos no repetidos.
set2 = a & b  # Valores que se repiten.
set3 = a - b  # Quita los repetidos en el segundo.
set4 = a ^ b  # Diferencia simétrica, valores unicos.










