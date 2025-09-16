##############################################################################
#                                                                            #
#Ej105.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:21 de mayo del 2024                                                   #
#                                                                            #
#Proposito:Un programa que calcula el sumatorio de todos los números hasta   #
#          el número que le digas                                            #
#                                                                            #
##############################################################################
print('Este programa te calculara el sumatorio desde el número que indiques'
      ' hasta el número que le digas.')

n = float(input('Indica en que número: '))
m = float(input('Indica en que otro número: '))

if n > m:
    print('El primer numero debe ser menor que el segundo.')

else:
    Sumatorio = 0

    while n <= m:
        Sumatorio += n
        n += 1

    print('El sumatorio es {0}.'.format(int(Sumatorio)))
