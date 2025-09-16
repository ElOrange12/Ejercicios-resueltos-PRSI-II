##############################################################################
#                                                                            #
#Ej073.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:5 de noviembre del 2024                                               #
#                                                                            #
#Proposito:Este programa identifica entre si el segundo número es el         #
#          cuadrado menor que el cuadrado y mayor que el cuadrado respecto   #
#          del primero.                                                      #
#                                                                            #
##############################################################################

n1 = float(input('Dime un número entero: '))
#"n1" es el primer número entero
n2 = float(input('Dime otro número entero: '))
#"n1" es el segundo número entero

cn1 = n1 ** 2
#"cn1" es el cuadrado del primer número enteroç

if n2 == cn1:
    print('El segundo número es el cuadrado del primero.')

elif n2 < cn1:
    print('El segundo número es menor que el cuadrado del primero.')

else:
    print('El segundo número es mayor que el cuadrado del primero.')
