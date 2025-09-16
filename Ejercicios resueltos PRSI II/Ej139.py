##############################################################################
#                                                                            #
#Ej139.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:4 de diciembre del 2024                                               #
#                                                                            #
#Proposito:Este programa muestra una función en base a tres valores y un     #
#          intervalo dados por el usuario.                                   #
#                                                                            #
##############################################################################
import turtle
import math

# Función para calcular las raíces de la ecuación cuadrática
def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return []  # No hay raíces reales
    elif discriminante == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return [x1, x2]

# Pedir valores al usuario
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
z1 = float(input("Introduce el límite inferior del intervalo (z1): "))
z2 = float(input("Introduce el límite superior del intervalo (z2): "))

# Calcular puntos para la función
x_values = [z1 + i * (z2 - z1) / 100 for i in range(101)]
y_values = [a * x**2 + b * x + c for x in x_values]

# Calcular los límites de la gráfica
y_min = min(y_values)
y_max = max(y_values)

# Configurar la pantalla
screen = turtle.Screen()
screen.setworldcoordinates(z1, y_min, z2, y_max)
screen.title("Gráfica de f(x) = ax^2 + bx + c")

# Configurar la tortuga
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Dibujar los ejes coordenados
pen.penup()
pen.color("blue")
pen.goto(z1, 0)
pen.pendown()
pen.goto(z2, 0)  # Eje X

pen.penup()
pen.goto(0, y_min)
pen.pendown()
pen.goto(0, y_max)  # Eje Y

# Dibujar la función
pen.penup()
pen.color("black")
pen.goto(x_values[0], y_values[0])
pen.pendown()
for x, y in zip(x_values, y_values):
    pen.goto(x, y)

# Calcular las raíces y dibujarlas
pen.color("red")
raices = calcular_raices(a, b, c)
for raiz in raices:
    pen.penup()
    pen.goto(raiz, 0)
    pen.dot(10, "red")  # Dibuja un círculo rojo en las raíces

# Mantener la ventana abierta
screen.mainloop()
