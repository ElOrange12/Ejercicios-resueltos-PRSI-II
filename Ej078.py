##############################################################################
#                                                                            #
#Ej078.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:21 de noviembre del 2024                                              #
#                                                                            #
#Proposito:Este programa halla el maximo de 5 números enteros.               #
#                                                                            #
##############################################################################

print('A continuación te preguntare 5 números enteros y te dire cual es el ma'
      'ximo')
print(' ')

a = float(input('Dime el 1º número: '))
b = float(input('Dime el 2º número: '))
c = float(input('Dime el 3º número: '))
d = float(input('Dime el 4º número: '))
e = float(input('Dime el 5º número: '))
#"a", "b", "c", "d" y "e" son los posibles números candidatos a ser el maximo.
print(' ')

cdt = a
#"cdt" es la variable candidato que irá cambiando para saber quien es el 
#maximo.

if b > cdt:
    cdt = b

if c > cdt:
    cdt = c

if d > cdt:
    cdt = d

if e > cdt:
    cdt = e

mx = cdt
#"mx" es el número definitivo que es el maximo.

print('El maximo de ({0}, {1:.0f}, {2:.0f}, {3:.0f}, {4:.0f}) es {5:.0f}.'
      .format(a, b, c, d, e, mx))
print(' ')
