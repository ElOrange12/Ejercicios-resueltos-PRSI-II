##############################################################################
#                                                                            #
#Ej100.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:17 de mayo del 2024                                                   #
#                                                                            #
#Proposito:Este programa muestra los multiplos de 6 entre 6 y 150            #
#                                                                            #
##############################################################################
print('A continuación te mostrare todos los multiplos de 6 entre 6 y 150')

i = 1

while (6 * i) <= 150:
    print(6 * i)
    i += 1

print('Hay',i - 1, 'múltiplos.')
