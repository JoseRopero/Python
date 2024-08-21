from flask import Flask

# Para ejecutar la aplicación escribimos en el terminal 'flask --app hello run'
# Nos dará una dirección local donde aparecerá el hello world

app = Flask(__name__)

@app.route("/")  # Python Decorators
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>Esto es un párrafo</p>'
            '<image src="https://media.giphy.com/media/7LXYYavB3TpsY/giphy.gif?cid'
            '=ecf05e479fchal7o5ovc95vkvg6no1zz9bv94ym4i2ffj3hh&ep=v1_gifs_search&rid=giphy.gif&ct=g"'
            'width=400>')


# ---------------------- Creación de decoradores -----------------------------------
# Un decorador es una función que toma otra función como argumento y extiende o modifica su comportamiento.
def make_bold(function):
    def wrapper():   # Esta función es la que envolverá (decorará) la función original
        return '<b>' + function() + '</b>'

    return wrapper


def make_emphasis(function):
    def wrapper():
        return '<em>' + function() + '</em>'

    return wrapper


def make_underlined(function):
    def wrapper():
        return '<u>' + function() + '</u>'

    return wrapper


# ---------------------------------------------------------------------------------------------------

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'bye'


@app.route('/username/<name>/<int:number>')  # Uso de rutas variables
def greet(name, number):
    return f'Hello {name}, you are {number} years old'


# Comprobará que el archivo actual es donde se encuentra el código de la aplicación

if __name__ == "__main__":  # Esto sustituye la escritura por terminal.
    app.run(debug=True)  # Debug True para no tener que parar la aplicación cada vez que hagamos un cambio.
