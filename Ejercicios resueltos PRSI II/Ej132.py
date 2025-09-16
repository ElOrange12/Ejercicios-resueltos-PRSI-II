##############################################################################
#                                                                            #
#Ej132.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:28 de noviembre del 2024                                              #
#                                                                            #
#Proposito:Este programa identifica si un número es primo o no.              #
#                                                                            #
##############################################################################

número = int(input('Dame un número: '))

if número > 1:
    creo_que_es_primo = True
    for divisor in range(2, número//2):
        if número % divisor == 0:
            creo_que_es_primo = False
            break
else:
    creo_que_es_primo = False

if creo_que_es_primo:
    print('El número {0} es primo.'.format(número))
else:
    print('El número {0} no es primo.'.format(número))
