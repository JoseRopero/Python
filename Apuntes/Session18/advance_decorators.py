class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):  # Esta función es la que envolverá (decorará) la función original
        # Verificamos si el primer argumento pasado a la función decorada tiene el atributo True
        if args[0].is_logged_in == True:
            function(args[0])  # Si el usuario está autenticado, se llama a la función original pasándole el argumento
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f'This is {user.name} new blog post.')


new_user = User('Jose')
new_user.is_logged_in = True
create_blog_post(new_user)
