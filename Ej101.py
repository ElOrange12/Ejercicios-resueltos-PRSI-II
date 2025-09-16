##############################################################################
#                                                                            #
#Ej101.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:17 de mayo del 2024                                                   #
#                                                                            #
#Proposito:Este programa muestra los multiplos de n entre n y m              #
#                                                                            #
##############################################################################
print('Este programa hara los múltiplos del numero que le digas hasta el tope'
      ' del número que digas por el producto')

n = float(input('Dime un número cualquiera: '))
m = float(input('Dime otro numero cualquiera como maximo de multiplicaciones: '))

print('A continuación te mostraré todos los múltiplos de', n,'entre', n,'y',
      n * m)

i = n

while i <= (m * n):
    print('{0}'.format(int(i)))
    i += n

print('Hay',(i / n) - 1, 'múltiplos.')
