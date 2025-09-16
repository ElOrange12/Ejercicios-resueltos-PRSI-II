##############################################################################
#                                                                            #
#Ej105_2.0.py                                                                #
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

n = -1
m = -2

while n >= m or n < 0 or m < 0:
    n = float(input('Indica en que número empieza: '))
    m = float(input('Indica en que otro número acaba: '))

    if n >= m:
        print('El primer numero debe ser menor que el segundo.')

    if n < 0 or m < 0:
        print('Los dos números tienen que ser positivos')

Sumatorio = 0

while n <= m:
    Sumatorio += n
    n += 1

print('El sumatorio es {0}.'.format(int(Sumatorio)))
