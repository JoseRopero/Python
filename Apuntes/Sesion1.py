# Sesión 1.

# 1. Salidas
print("SALIDAS:")
print("Hola mundo\nMi nombre es Jose")  # Con '\n' hacemos un salto de linea.
dato = 5
dato2 = 6
print("El dato es: {0}".format(dato))  # Esta es una manera de imprimir la variable.
print(f"El dato es: {dato}")  # Otra manera de darle formato.
print("Otra formato : %d" % dato)  # Otro formato: %s, %f, %d
print(f"Para limitar los dígitos de los decimales {dato} / {dato2} = {dato / dato2:.2f}")
print()

# 2. Operaciones con str.
print("OPERACIONES CON STR:")
cadena = 'hola, Vamos a empezar con Python'
longitudC = len(cadena)  # Para saber la longitud de una cadena.
print(f"La longitud de la cadena es: {longitudC}")
print(f"La variable es de tipo: {type(cadena)}")  # Con type nos muestra el tipo de variable.
print(cadena.capitalize())  # Con capitalize, la primera letra en mayúsculas y las demás las pasa a minúsculas.
print(cadena.title())  # En mayúsculas la primera letra de cada palabra.
print(cadena.lower())  # Todas en minúsculas
print(cadena.upper())  # En mayúsculas.
print(f"Cuantas veces aparece 'ho': {cadena.count('ho')}")  # El método count() retorna n veces aparece String.
print(f"La cadena termina en on: {cadena.endswith('on')}")
print(f"Reemplazamos la primera palabra: {cadena.replace('hola', 'Guay')}")  # Reemplaza la palabra.
print(f"Buscamos la palabra 'Vamos': {cadena.find('Vamos')}")  # Busca una palabra.
print(f"Primera aparición en la cadena de P: {cadena.index('P')}")
multiString = '''Hola, vamos con Python y las,
multilínea.
Otra manera de escribir texto en Python.
'''
print(multiString)  # Multilínea
cadenaCharacter = "Jose"
a, b, c, d = cadenaCharacter  # Pasar un String a una secuencia de caracteres.
print(a)
print(b)
print(c)
print(d)
print()
print(cadena[0])  # Accediendo a los caracteres del String por el índice.
print(cadena[-1])  # El último carácter.
ultimoIndice = len(cadena) - 1  # Sacamos el último índice de la cadena
print(ultimoIndice)
print(cadena[0:4])  # El primer número es el índice por el que empieza y el segundo es el término pero sin incluirlo.
print(cadena[::-1])  # El tercer número es el step. En este caso es como un reverse del String.
print(cadena[::2])

listaTexto = cadena.split()  # Pasa la cadena a una lista.
print(f"Pasamos una cadena a lista: {listaTexto}")
cadena2 = ' '.join(listaTexto)  # Pasa una lista a una cadena con espacios.
cadena3 = '-'.join(listaTexto)  # Entre las comillas podemos poner lo que queramos
print(cadena3)
print()

# 3. Conversiones de datos.
print("CONVERSIONES:")
n = int("25")
print(n)
stringN = str(n)
print("El numero es: " + stringN)  # Con los string podemos usar la concatenación.
n1 = abs(-9)  # Valor absoluto
print(f"El valor absoluto: {n1}")
print()

# 4. Trabajamos con las listas. Tipo de colección ordenada y modificable. Admite duplicados.
print("LISTAS:")
vacio = []  # Se puede crear una lista vacía.
vacio2 = list()
lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'x', 'm']  # De esta manera inicializamos una lista.
lista4 = ['a', 5, "Hola como estas", {'Country': 'España', 'City': 'Málaga'}]  # Pueden tener distintos datos.
# Ejemplos desempaquetar elementos de una lista
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Desempaquetando
print(f"{first} {second} {third} {rest} {tenth}")
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

lista1.remove('c')  # Eliminamos un elemento de la lista.
lista2 = ['g', 'h', 'i', 'j', 'k', 'l']
lista1.append(lista2)  # Añadimos la lista2 a la lista1 (lista anidada).
print(f"Lista anidada: {lista1}")
lista1.insert(2, 'c')  # Para introducir un valor en el índice indicado. No sustituye.
print(f"Añadimos un elemento a la lista en el indice 2: {lista1}")
lista1.extend(['o', 'p', 'q'])  # Añade una lista de elementos a la original.
print(f"Extendemos la lista: {lista1}")
print(f"Ultimo elemento de la lista: {lista1[-1]}")  # Imprime el último elemento de la lista.
print(f"Imprimo por rangos: {lista1[0:3]}")  # Imprime por rangos. El segundo parámetro no esta incluido, llegaría al 2.
print(lista1[:3])  # Es lo mismo que la línea anterior.
print(lista1[2:])  # Imprime desde el segundo elemento hasta el final.
print(f"Está la letra 'd' en  la lista? {'d' in lista1}")  # Devuelve true o false si el elemento esta en la lista.
print(f"Cuantas veces aparece la letra 'x': {lista1.count('x')}")
lista1.pop()  # Elimina el último elemento de la lista si no indicamos el índice.
print(lista1)
# del lista1[2] -> Elimina por índice
# del lista1[2:4] -> Elimina por rangos
# del lista1 → Elimina la lista
lista3 = lista1 * 2  # Duplicamos la lista.
print(f"Duplicamos la lista: {lista3}")
lista3.reverse()
print(f"Reverse: {lista3}")
lista3.clear()  # Vacía la lista.
lista3 = [5, 9, 10, -4, 3, 59]
print(lista3)
lista3.sort()  # Ordenamos la lista.
print(f"Ordenamos la lista: {lista3}")
lista3.sort(reverse=True)
print(f"Revertimos la lista: {lista3}")
print()

# 5. Tupla. Tipo de colección ordenada e inmutable. Permite duplicados.
print("TUPLA:")
tupla = ('a', 'b', "Hola", 'c', 5, 6, 5.98, [1, 2, 3, 4], 'd', 'e')  # Inicializamos una tupla.
print(tupla)
print(tupla[-2])  # Imprime desde el final de la tupla.
print(len(tupla))  # Longitud de la tupla. 
lista4 = list(tupla)  # Pasamos la tupla a una lista.
print(lista4)
tupla1 = tuple(lista4)  # Pasamos la lista a una tupla.
print(tupla1)
print()

# 6. Diccionario. Tipo de colección desordenada, modificable e indexada. No hay duplicados.
print("DICCIONARIO:")
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # Inicializamos un diccionario.
print(diccionario['a'])  # Imprime el valor de la clave.
resultado = diccionario['a']  # Asignamos el valor a la variable.
diccionario['c'] = 54  # Cambiamos el valor de la clave.
diccionario.pop('d')  # Elimina la clave valor.
del diccionario['a']  # Otra manera de eliminar.
print()

# 7. Conjuntos(set). Colección desordenada, no indexada e inmutable pero podemos agregar nuevos elementos. No duplicados
print("SETS:")
a = {1, 2, 3, 4, 5}  # Inicializamos un set (Conjuntos). No se pueden repetir los elementos.
b = {2, 5, 9, 8, 10}
set1 = a | b  # Une los elementos no repetidos.
set2 = a & b  # Valores que se repiten.
set3 = a - b  # Quita los repetidos en el segundo.
set4 = a ^ b  # Diferencia simétrica, valores unicos.
