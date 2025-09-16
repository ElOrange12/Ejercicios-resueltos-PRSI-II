##############################################################################
#                                                                            #
#Ej50.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:9 de mayo del 2024                                                    #
#                                                                            #
#Proposito:Este programa hara un diagrama de sectores mediante las           #
#          respuestas del usuario                                            #
#                                                                            #
##############################################################################
from turtle import Screen, Turtle

#Calificaciones
Suspensos = float(input('¿Cuántos suspensos hay?: '))
Aprobados = float(input('¿Cuántos aprobados hay?: '))
Notables = float(input('¿Cuántos notables hay?: '))
Sobresalientes = float(input('¿Cuántos sobresalientes hay?: '))

#Calificaciones totales
Ct = Suspensos + Aprobados + Notables + Sobresalientes

#"r" es el radio del diagrama de sectores
r = 300

#Inicialización
pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)
tortuga.hideturtle()

#Dibujo del circulo exterior
tortuga.penup()
tortuga.goto(0, -r)
tortuga.pendown()
tortuga.pensize(2)
tortuga.circle(r)
tortuga.penup()
tortuga.home()
tortuga.pendown()

#Sector suspensos
ángulo = 360 * Suspensos / Ct
tortuga.left(ángulo)
tortuga.forward(r)
tortuga.backward(r)

#Nombre del sector suspensos
tortuga.penup()
tortuga.right(ángulo / 2)
tortuga.forward(r / 2)
tortuga.write('Suspensos', font = ('Arial', 15, 'normal'))
tortuga.backward(r / 2)
tortuga.left(ángulo / 2)
tortuga.pendown()

#Sector aprobados
ángulo = 360 * Aprobados / Ct
tortuga.left(ángulo)
tortuga.forward(r)
tortuga.backward(r)

#Nombre del sector suspensos
tortuga.penup()
tortuga.right(ángulo / 2)
tortuga.forward(r / 2)
tortuga.write('Aprobados', font = ('Arial', 15, 'normal'))
tortuga.backward(r / 2)
tortuga.left(ángulo / 2)
tortuga.pendown()

#Sector notables
ángulo = 360 * Notables / Ct
tortuga.left(ángulo)
tortuga.forward(r)
tortuga.backward(r)

#Nombre del sector suspensos
tortuga.penup()
tortuga.right(ángulo / 2)
tortuga.forward(r / 2)
tortuga.write('Notables', font = ('Arial', 15, 'normal'))
tortuga.backward(r / 2)
tortuga.left(ángulo / 2)
tortuga.pendown()

#Sector sobresalientes
ángulo = 360 * Sobresalientes / Ct
tortuga.left(ángulo)
tortuga.forward(r)
tortuga.backward(r)

#Nombre del sector Sobresalientes
tortuga.penup()
tortuga.right(ángulo / 2)
tortuga.forward(r / 2)
tortuga.write('Sobresalientes', font = ('Arial', 15, 'normal'))
tortuga.backward(r / 2)
tortuga.left(ángulo / 2)
tortuga.pendown()

pantalla.exitonclick()
