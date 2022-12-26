from turtle import Turtle, Screen, colormode
import random

t = Turtle()  # Inicializamos nuestra tortuga
t.shape("turtle")  # Cambiamos su forma, su forma original es una flecha
t.color("blue")  # y el color (https://cs111.wellesley.edu/reference/colors)

# Ejercicio. Dibuja un cuadrado de 100x100
for _ in range(4):
    t.fd(100)
    t.rt(90)

t.rt(180)

# Dibujar una linea discontinua.
for _ in range(20):
    t.fd(10)
    t.penup()
    t.fd(10)
    t.pendown()

# Dibujar un triángulo, cuadrado, pentágono, hexágono, octógono y decágono con distintos colores.
t.reset()
num_lados = 3  # Empezamos con el triángulo y en el bucle incrementamos el número de lados
angulo = 360  # El ángulo de cada figura es de 360 entre el número de lados
colormode(255)
while num_lados <= 10:
    for _ in range(num_lados):
        t.fd(100)
        t.rt(angulo / num_lados)
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    num_lados += 1

# Dibuja un paseo aleatorio
t.reset()
direcciones = [0, 90, 180, 270]
colormode(255)
t.pensize(10)
t.speed(0)
for _ in range(50):
    t.setheading(random.choice(direcciones))
    t.fd(30)
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Dibujar un Spirograph
t.reset()
t.speed(0)
for inclinacion in range(0, 360, 5):
    t.setheading(inclinacion)
    t.circle(100)
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


s = Screen()  # Creamos una ventana donde aparecerá nuestra tortuga
s.exitonclick()  # Con este método la ventana no se cierra hasta que hagamos click.
