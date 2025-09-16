##############################################################################
#                                                                            #
#Ej84.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:21 de noviembre del 2024                                              #
#                                                                            #
#Proposito:Este programa calcula la cantidad de años que se deberia esperar  #
#          para conseguir un capital con una inversión dada y un interes     #
#          tambien dado.                                                     #
#                                                                            #
##############################################################################
from math import log10

print('A continuación se calculara los años que se podrá conseguir un capital' 
      ' dado por el usuario, partiendo de una inversión y un interes también '
      'dado por el usuario.')
print(' ')

Cf = -1
C = -1
x = -1

while Cf < 0:
    Cf = float(input('Dime el capital que se quiere obtener: '))
    if Cf < 0:
        print('El capital no puede ser negativo.')

while C < 0:
    C = float(input('Cual es la inversión que se quiere hacer: '))
    if C < 0:
        print('La inversión no puede ser negativa.')

while x < 0:
    x = float(input('Que interes anual tiene: '))
    if x < 0:
        print('El interes no puede ser negativo.')

print(' ')


Num = log10(Cf) - log10(C)
Den = log10(1 + x/100)
#"Num" y "Den" son el numerador y el denominador de la F(x) para sacar los 
#años que se tarda en conseguir

n = 0
#"n" es el número de años que se tarda en conseguir el capital final

if Num == 0:
    print('Para obtener {0:.0f}€ con una inversión de {1:.0f}€ no hay que'
          ' esperar nada, sea cual sea el interés'.format(Cf, C))
elif Den == 0:
    print('Obtener {0:.0f}€ con una inversión de {1:.0f} al {2:.0f}%'' an'
          'ual es imposible.'.format(Cf, C, x))
else:
    n = Num/Den

    print('Para obtener {0:.0f}€ con una inversión de {1:.0f}€ al {2:.0f}% '
          'anual es necesario esperar {3:.4f} años.'.format(Cf, C, x, n))

print(' ')
