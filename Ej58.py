##############################################################################
#                                                                            #
#Ej58.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:15 de mayo del 2024                                                   #
#                                                                            #
#Proposito:Te dice si un numero es positivo                                  #
#                                                                            #
##############################################################################
print('Te preguntaremos un número y te diremos si es positivo')

N = float(input('Dime el numero: '))
#"N" es el numero que nos dicen

if not N < 0:
    print('El número es positivo')
