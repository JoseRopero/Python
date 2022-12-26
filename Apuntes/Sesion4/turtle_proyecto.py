from turtle import Turtle, Screen, colormode
import random
import colorgram  # Paquete instalado


colores = colorgram.extract('imagen.jpg', 30)
colores_rgb = []
for indice in range(30):
    red = colores[indice].rgb.r
    green = colores[indice].rgb.g
    blue = colores[indice].rgb.b
    rgb = (red, green, blue)
    colores_rgb.append(rgb)
# Del for sacamos esta lista de colores. Hago copy paste y lo meto en una lista.
lista_rgb = [(238, 251, 243), (242, 230, 68), (184, 18, 42), (253, 235, 240), (219, 238, 244),
             (188, 72, 35), (16, 139, 83), (113, 180, 207), (191, 179, 21), (23, 121, 168), (24, 38, 74), (219, 60, 97),
             (241, 232, 2), (212, 161, 92), (75, 174, 96), (180, 44, 62), (37, 45, 112), (15, 165, 212),
             (220, 130, 157), (216, 71, 51), (125, 184, 123), (6, 59, 38), (166, 27, 24), (9, 94, 54), (238, 157, 178),
             (147, 208, 221), (5, 85, 111), (160, 212, 182), (237, 170, 163)]


t = Turtle()
t.hideturtle()
colormode(255)
t.penup()
subida = -200
t.goto(-200, subida)  # Posicionamos el puntero
for colum in range(10):
    for linea in range(10):
        t.dot(20, random.choice(lista_rgb))  # Marcamos el punto y movemos 50 pasos para marcar otro punto
        t.penup()
        t.fd(50)
    t.penup()  # Después de terminar la línea, subimos el puntero y volvemos a recorrer la fila.
    subida += 50
    t.goto(-200, subida)

s = Screen()
s.exitonclick()
