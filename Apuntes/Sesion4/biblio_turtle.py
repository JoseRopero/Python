from turtle import Turtle, Screen

pepito = Turtle()  # Inicializamos nuestra tortuga
pepito.shape("turtle")  # Cambiamos su forma, su forma original es una flecha
pepito.color("coral")  # y el color

pepito.forward(100)  # Hacemos que se mueva 100 pasos
pepito.circle(60)

mi_ventana = Screen()  # Creamos una ventana donde aparecerá nuestra tortuga
print(mi_ventana.canvheight)  # Imprimimos la ventana
mi_ventana.exitonclick()  # Con este método la ventana no se cierra hasta que hagamos click.
