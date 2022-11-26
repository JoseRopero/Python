# Condicionales
'''
<  Menor que
<= Menor o igual
>  Mayor que
>= Mayor o igual
== Igualación
!= Distinto
'''

a = 5
b = 6
c = 7

resultado = (a > 5 and c < 7)  # Devuelve True o False.
print(f"Ejemplo de condicional: {resultado}")
print("")

# TABLA DE LA VERDAD
# and
print("\tTABLA DE LA VERDAD")
print("and:")
print('True and true=', True and True)
print('True and False=', True and False)
print('False and True=', False and True)
print('False and False=', False and False)

print("")

# or
print("or: ")
print('True or true=', True or True)
print('True or False=', True or False)
print('False or True=', False or True)
print('False or False=', False or False)

print('')

resultado = ((a >= 5 or c < 7) and (b == 5))
print(resultado)
print("")

# is, is not, in, not in

# print('1 is 1', 1 is 1)                   # True - evalua si los dos son iguales
# print('1 is not 2', 1 is not 2)           # True - evalua si son distintos
print('A in Asabeneh', 'A' in 'Asabeneh') # True - encuentra 'a' en el string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - La 'B' mayuscula no se encuentra en el string
print('coding' in 'coding for all') # True - Encuentra la palabra
print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print("==================================================================================================")

# Sentencias condicionales.
print("\tSentencias condicionales")
# if
print("if: ")

a = 5
b = 6

if a >= 5 and b <= 6:  # En el if hay que tener cuidado con la tabulacion y espacios.
    print('a es mayor o igual que cinco y b es menor o igual que 6')
elif a >= 6:
    print('a es mayor o igual que seis')
else:
    print("No ha introducido un mumero")
print('Fin del if')

print("")
print("Short hand")  # Forma corta del if
print("a es mayor o igual que cinco y b es menor o igual que 6") if a >= 5 and b <= 6 else print("No ha introducido un mumero")
print("")

letra = input("Introduzca un carácter: ").lower()  # Pasamos a minúsculas para no comparar minúsculas y mayúsculas.

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Es una vocal")
else:
    print("No es una vocal")
    
print("")
print("===============================================================================================================")
# while
print("while:")
contador = 1
while contador <= 10:  # Mientras la condicion sea True.
    if contador % 2 == 0:  # Sacamos los pares.
        print(f'{contador} es par')
    contador += 1

print('')
print("==============================================================================================================")
# Palabras reservadas break y continue

contador2 = 1
while contador2 <= 10:
    print(f'Contador vale: {contador2}')
    if contador2 == 5:
        break  # Rompe el bucle
    contador2 += 1
print('Estamos fuera del bucle')

print('')

contador3 = 0
while contador3 <= 10:  # Mientras la condicion sea True.
    contador3 += 1
    if contador3 % 2 == 0:
        print(f'{contador3} es par')
        continue  # Todo lo que hay por debajo del continue no se ejecuta y vuelve a evaluar la expresion.
        # En este caso hemos creado un bucle infinito.
    print(f'Valor de contador: {contador3}')

print('')
print("=============================================================================================================")
# for

lista = [1, 2, 3, 4, 'a', 6, 7, 8]

longitud = len(lista)  # Longitud de la lista
print(f'La longitud de la lista: {longitud}')

for palabra in lista:  # Recorremos la lista buscando una palabra
    print(f'La palabra actual es: {palabra}')
    if palabra == 'a':
        print(f'He encontrado el caracter {palabra}')
        break
# Otra manera de hacerlo
if 'a' in lista:
    print(f'He encontrado el caracter')

if 'b' not in lista:
    print('No esta en la lista')

lista5 = [5, 1, 15, 8, 20, 2]

listaOrdenada = sorted(lista5)  # Ordenamos la lista ascendente.
listaReverse = sorted(lista5, reverse=True)  # lista reverse.
print(listaOrdenada)
print(listaReverse)

tupla = (1, 2, 3, 4, 'a', 'b')

for valorActual in lista:  # Iteramos sobre cada elemento de la lista y lo guarda en la variable valorActual.
    print(valorActual)  # Después lo imprime

print('')

for valorActual1 in tupla:  # Iteramos sobre cada elemento de la tupla y lo guarda en la variable valorActual.
    print(valorActual1)  # Después lo imprime

print('')

for numero in range(10):  # Valor inicial e incluido 0 y valor final 10 excluido
    print(numero)
print('')
for numero1 in range(5, 10):  # Valor inicial e incluido 5 y valor final excluido 10.
    print(numero1)

print("=============================================================================================================")
# Match

valor = 4

match valor:
    case 1:
        print('Valor es 1')
    case 2:
        print('Valor es 2')
    case 3:
        print('Valor es 3')
    case 4:
        print('Valor es 4')

encontrado = False   # Se denomina variable bandera.

for numero5 in lista5:
    if numero5 == 15:
        encontrado = True
        break

if encontrado:
    print('Numero encontrado')
else:
    print('Numero no encontrado')

# Otra manera de hacerlo:

for numero5 in lista5:
    if numero5 == 15:
        print('Encontrado')
        break
else:
    print('No encontrado')




