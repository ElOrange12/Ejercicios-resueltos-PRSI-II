##############################################################################
#                                                                            #
#Ej038.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:2 de mayo del 2024                                                    #
#                                                                            #
#Proposito:Un programa que calcule el área y perímetro de triángulo          #
#                                                                            #
##############################################################################
from math import sqrt

a = float(input('Dime un lado del triángulo: '))
b = float(input('Dime el segundo lado del triángulo: '))
c = float(input('Dime el tercer lado del triángulo: '))
#"a", "b" y "c" son los lados del triángulo

p = a + b + c
#"p" es el perimetro del triángulo

s = (a + b + c)/2
#"s" es el semiperimetro del triángulo
A = sqrt(s*(s - a)*(s - b)*(s - c))
#"A" es el area del triángulo

print('El perímetro del triángulo de lados {0}, {1} y {2} es {3} y el área es'
      ' {4}.'.format(a, b, c, p, A))
