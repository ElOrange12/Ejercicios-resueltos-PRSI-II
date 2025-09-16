##############################################################################
#                                                                            #
#Ej037.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:2 de mayo del 2024                                                    #
#                                                                            #
#Proposito:Un programa que calcule el área de triángulo                      #
#                                                                            #
##############################################################################

b = float(input('Introduce la base del triángulo: '))
#"b" es la base del triángulo

h = float(input('Introduce la altura del triángulo: '))
#"h" es la altura del triángulo

a = (b*h) / 2

print('El área del triángulo de base {0} y altura {1} es {2:.2f}.'
      .format(b, h, a,))
