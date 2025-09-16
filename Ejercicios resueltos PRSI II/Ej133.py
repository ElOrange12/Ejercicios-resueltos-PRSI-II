##############################################################################
#                                                                            #
#Ej133.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:2 de diciembre del 2024                                               #
#                                                                            #
#Proposito:Este programa identifica si un número es primo o no.              #
#                                                                            #
##############################################################################
from math import sqrt

número = int(input('Dame un número: '))
#Sacamos la parte entera de la raiz del número.
Rnúmero = int(sqrt(número))

if número > 1:
    creo_que_es_primo = True
    #Ponemos la nueva variable en el rango del "for" y le sumamos 1 para que
    #entre en el rango.
    for divisor in range(2, Rnúmero + 1):
        if número % divisor == 0:
            creo_que_es_primo = False
            break
else:
    creo_que_es_primo = False

if creo_que_es_primo:
    print('El número {0} es primo.'.format(número))
else:
    print('El número {0} no es primo.'.format(número))
