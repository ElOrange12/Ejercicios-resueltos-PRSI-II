##############################################################################
#                                                                            #
#Ej106.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:22 de mayo del 2024                                                   #
#                                                                            #
#Proposito:Este programa calcula el factorial de un número                   #
#                                                                            #
##############################################################################
print('Este programa calculara el factorial del número que le digas')

n = -1

while n < 0:
    n = float(input('Dime un múmero: '))
    m = 1
    #"m" es el resultado del facotiral

    if n < 0:
        print('El numero debe ser positivo')

    else:
        while n > 0:
            m *= n
            n -= 1

        print('El factorial es {0}.'.format(int(m)))
