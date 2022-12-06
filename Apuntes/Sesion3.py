miTemperatura = 27.0  # Variable global, puede usarse desde cualquier sitio


def mifuncion():  # Las funciones deben cargarse antes de usarse.
    # global miTemperatura -> Con la palabra reservada 'global' podemos cambiar el valor a la variable original.
    miTemperatura = 32  # Variable Shadowing. Declaro una variable local con el mismo nombre que la global.
    print('Hola')
    print(f'Fuera hace {miTemperatura}')
    for i in range(0, 9):
        print(i)


def mifuncion2(nombre):  # Variable local. Esta variable solo puede ser usada en esta función.
    print(f'Mi nombre: {nombre}')


def mifuncion3(nombre='Mercedes'):  # Parámetro opcional.
    print(f'Mi nombre: {nombre}')  # Podría llamar a la función sin parámetro e imprimiría 'Mercedes'


def matematicas(a, b):  # Funciones anidadas.
    def suma(sumando1, sumando2):
        print(sumando1 + sumando2)

    def resta(numero1, numero2):
        print(numero1 - numero2)

    suma(a, b)
    resta(a, b)


def suma2(a=5, b=2, c=10):  # Parámetros opcionales.
    """Esto es un Docstring para la documentación."""
    print(a + b + c)


def suma3(*args):  # Parámetro variable
    resultado = 0
    for i in args:
        resultado += i
    print(resultado)


def diccionario(**kwargs):  # Parámetro diccionario
    for key, value in kwargs.items():  # Para iterar sobre un diccionario.
        print(key, '=', value)


def suma4(a, b):
    return a + b  # Con la palabra reservada 'return' devolvemos un valor.


def suma5(a, b):
    return a + b, a - b, a * b, a / b
    # Nos devuelve una tupla con los resultados. Si la invocamos con varias variables, se les asignara a cada una.


def sumador(**kwargs):
    inicial = kwargs[
        'inicial'] if 'inicial' in kwargs else 0  # Operador ternario. Si no pasáramos parámetro, lo tendría controlado.
    final = kwargs['final'] if 'final' in kwargs else 15  # Operador ternario.

    resultado = 0
    for x in range(inicial, final + 1):
        resultado += x
    return resultado


anonima = lambda: print('Hola')  # Función anónima(lambda).
anonima2 = lambda nombre: print('Hola', nombre)  # lambda con parámetros
anonima3 = lambda x: x + x  # No se le pone el return.

# ---------------------------------------------------------------------------#


print('Antes')
mifuncion()
print('Después')
mifuncion2('Jose')
mifuncion3()
matematicas(5, 2)
suma2(c=9)
suma2(b=18, a=20, c=9)
suma3(1)
suma3(1, 5)
suma3(1, 5, 1)
suma3(1, 5, 1, 58, 6, 20, 10)
diccionario(vivienda='piso', coche='Seat')
print(suma5(8, 2))
suma, resta, multi, divi = suma5(8, 2)
print(f'la suma: {suma}, la resta: {resta}, la multiplicación: {multi}, la division: {divi}')
print(sumador(inicial=15, final=50))
print(sumador(inicial=8))
anonima()
