##############################################################################
#                                                                            #
#Ej44.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:7 de mayo del 2024                                                    #
#                                                                            #
#Proposito:Un programa que dibuje dos cuadrados uno dentro del otro          #
#                                                                            #
##############################################################################
from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 255)
pantalla.screensize(400, 200)

tortuga = Turtle()
tortuga.penup()
tortuga.left(180)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.pendown()

tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)

tortuga.penup()
tortuga.left(180)
tortuga.forward(50)
tortuga.right(90)
tortuga.forward(50)
tortuga.pendown()

tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

pantalla.exitonclick()
