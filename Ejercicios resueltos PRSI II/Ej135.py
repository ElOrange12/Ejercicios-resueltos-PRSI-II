##############################################################################
#                                                                            #
#Ej135.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:2 de diciembre del 2024                                               #
#                                                                            #
#Proposito:Muesta la función coseno en un rango determinado por el usuarsio. #
#                                                                            #
##############################################################################
from turtle import Screen, Turtle
from math import cos, pi

x1 = float(input('Dime el límite inferior del interior: '))
x2 = float(input('Dime el límite superior del interior: '))
puntos = int(input('Dime cuántos puntos he de mostrar: '))

pantalla = Screen()
pantalla.setup(825, 425)
pantalla.screensize(800, 400)
pantalla.setworldcoordinates(x1, -1, x2, 1) 

tortuga = Turtle()
x = x1
dx = (x2 - x1) / puntos
tortuga.penup()
tortuga.goto(x, cos(x))
tortuga.pendown()
while x <= x2:
    tortuga.goto(x, cos(x))
    x += dx

pantalla.exitonclick()
