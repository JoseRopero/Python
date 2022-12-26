from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forwards():
    t.fd(10)


s.listen()  # Para empezar a usar eventos de pantalla
# Un receptor de eventos para escuchar la tecla que pulsemos.
# Ejemplo de una función de orden superior. Una función que tiene como parámetro otra función.
s.onkey(key="space", fun=move_forwards)  # Como parámetros necesita una función sin argumentos y una key.
s.exitonclick()
