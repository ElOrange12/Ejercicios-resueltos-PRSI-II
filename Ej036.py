##############################################################################
#                                                                            #
#Ej036.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:30 de abril del 2024                                                  #
#                                                                            #
#Proposito:Un programa que calcule el perimetro y el área de un rectángulo   #
#                                                                            #
##############################################################################

b = float(input('Introduce la base del rectángulo: '))
#"b" es la base del rectángulo

h = float(input('Introduce la altura del rectángulo: '))
#"h" es la altura del rectángulo

p = 2*b + 2*h

print('El perimetro del rectángulo de base {0} y altura {1} es {2:.2f}.'
      .format(b, h, p))

a = b * h

print('Y su area del rectángulo es {0:.2f}.'.format(a))
