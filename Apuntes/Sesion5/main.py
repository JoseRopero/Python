class User:  # Con la palabra reservada 'class' creamos una clase.

    # Por convención en las clases se usa PascalCase y para lo demás snake_case

    def __init__(self, user_id, username):  # Este es el constructor de la clase, le pasamos los atributos
        self.user_id = user_id
        self.username = username
        self.followers = 0  # No siempre pasamos los atributos por el constructor.
        #  En este caso el atributo 'followers' siempre se inicializa con el objeto con valor 0.
        self.following = 0

    def follow(self, user):  # Ejemplo de método, el cual recibe un usuario al que seguimos (Instagram)
        user.followers += 1  # El usuario al que seguimos le sube los seguidores
        self.following += 1  # A nosotros aumenta los que seguimos.


user_1 = User("001", "Jose")
user_2 = User("002", "Mercedes")

user_1.follow(user_2)  # Uso del método.

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
