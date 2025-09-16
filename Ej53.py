##############################################################################
#                                                                            #
#Ej50.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:7 de noviembre del 2024                                               #
#                                                                            #
#Proposito:Este programa soluciona una ecuacion de primer grado              #
#                                                                            #
##############################################################################
print('Programa para la resolución de la ecuación a x + b = 0')

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

if a != 0:
    x = -b / a
    print('Solución:', x)

else:
    print('A no puede ser 0')
