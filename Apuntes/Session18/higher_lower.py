from flask import Flask
import random

app = Flask(__name__)

aleatorio = random.randint(0, 9)


@app.route("/")  # Python Decorators
def mayor_menor():
    return ('<h1>Adivina el número entre 0 y 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route('/<int:number>')
def comprobar_numero(number):
    print(aleatorio)
    if number < aleatorio:
        return ('<h1 style="color: red">Demasiado bajo, prueba otra vez!!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400>')
    elif number > aleatorio:
        return ('<h1 style="color: purple">Demasiado alto, prueba otra vez!!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400>')
    else:
        return ('<h1 style="color: green">Acertaste!!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400>')


if __name__ == "__main__":
    app.run(debug=True)
