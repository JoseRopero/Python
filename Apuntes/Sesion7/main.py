file = open('my_file.txt')   # Indicamos el archivo que queremos abrir, el modo por defecto es solo lectura
contenido = file.read()
print(contenido)
file.close()

print()
# Otra manera de abrir un archivo y no tener que indicar cuando cerrarlo es con la palabra 'with'
with open('my_file.txt') as file:
    contenido = file.read()
    print(contenido)

with open('my_file.txt', mode='a') as file:  # El modo 'a' append. 'w' write, pero sobreescribe el archivo.
    file.write("\nTexto nuevo")

# Si no existe el archivo lo crea nuevo.
with open('new_my_file.txt', mode='w') as file:
    file.write("Nuevo texto")
