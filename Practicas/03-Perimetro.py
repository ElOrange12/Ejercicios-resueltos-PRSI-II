##############################################################################
#                                                                            #
#perimetro.py                                                                #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:24/4/24                                                               #
#                                                                            #
#Proposito:Un programa que calcule la longitud de una circunferencia         #
#                                                                            #
##############################################################################
from math import pi

r = float(input('Introduce el radio de la circunferencia: '))
#"r" es el radio de la circunferencia de la que queremos calcular su perimetro

p = 2 * pi * r
#"p" es el perimetro de la circunferencia que nos han dado

print('La longitud de la circunferencia de radio {0} es {1:.2f}'.format(r, p))
