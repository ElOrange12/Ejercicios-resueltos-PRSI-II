##############################################################################
#                                                                            #
#grafico.py                                                                  #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:3 de mayo del 2024                                                    #
#                                                                            #
#Proposito:Un programa que crea una pantalla blanca y dibuja una flecha      #
#          la derecha                                                        #
#                                                                            #
##############################################################################
from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

tortuga = Turtle()
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

tortuga.penup()
tortuga.right(90)
tortuga.forward(100)
tortuga.pendown()

tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

pantalla.exitonclick()
