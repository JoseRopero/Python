# try, except, else, finally, raise

# FileNotFound

try:
    file = open("a_file.txt")  # En este punto daría un error porque no existe el archivo.
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:  # Especificamos que tipo de error queremos captar.
    file = open("a_file.txt", "w")  # Entraría esta línea y crearía el archivo.
    file.write("algo")
except KeyError as error_message:  # Recogemos el error en la variable y después lo muestro
    print(f"La clave {error_message} no existe")
else:  # Cuando no salta ninguna excepción se ejecuta este bloque
    content = file.read()
    print(content)
finally:  # Código que se va a ejecutar sin importar lo que haya pasado antes.
    file.close()
    print("File was closed")


# Cuando queremos lanzar una excepción usamos 'raise'
# Por ejemplo queremos calcular el IMC, pero al pedir la altura no debería de sobrepasar los 3 metros

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Un humano no debería de sobrepasar los 3 metros")

IMC = weight / height ** 2
print(IMC)
