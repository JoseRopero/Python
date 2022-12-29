class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):  # Ejemplo de herencia de clases
    def __init__(self):  # En el constructor llamamos al método super() y heredamos los atributos y métodos del padre.
        super().__init__()

    def breathe(self):  # Modificamos el método de la clase padre
        super().breathe()  # Hace lo mismo que el método padre, pero además añadimos otra función.
        print("Doing this underwater")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
