##############################################################################
#                                                                            #
#Ej43.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:7 de mayo del 2024                                                    #
#                                                                            #
#Proposito:Un programa que dibuje un triangulo equilatero mediante una       #
#          tortuga                                                           #
#                                                                            #
##############################################################################
from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

tortuga = Turtle()
tortuga.penup()
tortuga.left(180)
tortuga.forward(50)
tortuga.left(90)
tortuga.forward(43.3012701892)
tortuga.left(90)
tortuga.pendown()

tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)

pantalla.exitonclick()
