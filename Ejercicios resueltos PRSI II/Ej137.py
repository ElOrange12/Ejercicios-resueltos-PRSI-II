##############################################################################
#                                                                            #
#Ej137.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:4 de diciembre del 2024                                               #
#                                                                            #
#Proposito:Este programa muestra una función en un intevalo concreto.        #
#                                                                            #
##############################################################################
import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.setworldcoordinates(-2, -1.5, 2, 1.5)
screen.title("Gráfica de f(x) = 1 / (x + 1)")

# Configuración de la tortuga
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Dibujar los ejes
pen.penup()
pen.goto(-2, 0)
pen.pendown()
pen.goto(2, 0)  # Eje X
pen.penup()
pen.goto(0, -1.5)
pen.pendown()
pen.goto(0, 1.5)  # Eje Y

# Dibujar la función
pen.penup()
step = 0.04  # Incremento para los puntos
x = -2
pen.color("blue")

while x <= 2:
    if x != -1:  # Evitar x = -1
        y = 1 / (x + 1)
        pen.goto(x, y)
        pen.dot(4, "blue")  # Puntos azules para la función
    x += step

# Dibujar el punto problemático
pen.goto(-1, 0)
pen.dot(10, "red")  # Punto rojo en (-1, 0)

# Mantener la ventana abierta
screen.mainloop()
