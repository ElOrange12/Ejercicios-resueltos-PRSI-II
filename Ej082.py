##############################################################################
#                                                                            #
#Ej082.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:21 de noviembre del 2024                                              #
#                                                                            #
#Proposito:Este programa determina que punto es mas cerca del primero dado.  #
#                                                                            #
##############################################################################
from math import sqrt

print('A continuación de pedire cinco puntos, el 1º sera desde el que calcula'
      'remos la distancia y los demas seran 4 puntos distintos.')
print('Se preguntaran de manera que primero se preguntara su X y después se p'
      'reguntara su Y')
print(' ')

X1 = float(input('Dime del 1º punto su X: '))
Y1 = float(input('Ahora su Y: '))
print(' ')

X2 = float(input('Dime del 2º punto su X: '))
Y2 = float(input('Ahora su Y: '))
print(' ')

X3 = X2
Y3 = Y2
while X3 == X2 and Y3 == Y2:
    X3 = float(input('Dime del 3º punto su X: '))
    Y3 = float(input('Ahora su Y: '))
    if X3 == X2 and Y3 == Y2:
        print('El vector ({0:.0f}, {1:.0f}) ya lo has ingresado.'
              .format(X3, Y3))
    print(' ')

X4 = X2
Y4 = Y2
while X4 == X2 and Y4 == Y2 or X4 == X3 and Y4 == Y3: 
    X4 = float(input('Dime del 4º punto su X: '))
    Y4 = float(input('Ahora su Y: '))
    if X4 == X2 and Y4 == Y2:
        print('El vector ({0:.0f}, {1:.0f}) ya lo has ingresado.'
              .format(X4, Y4))
    elif X4 == X3 and Y4 == Y3:
        print('El vector ({0:.0f}, {1:.0f}) ya lo has ingresado.'
              .format(X4, Y4))
    print(' ')

X5 = X1
Y5 = Y1
while X5 == X2 and Y5 == Y2 or X5 == X3 and Y5 == Y3 or X5 == X4 and Y5 == Y4:
    X5 = float(input('Dime del 5º punto su X: '))
    Y5 = float(input('Ahora su Y: '))
    if X5 == X1 and Y5 == Y1:
        print('El vector ({0:.0f}, {1:.0f}) ya lo has ingresado.'
              .format(X5, Y5))
    if X5 == X2 and Y5 == Y2:
        print('El vector ({0:.0f}, {1:.0f}) ya lo has ingresado.'
              .format(X5, Y5))
    if X5 == X3 and Y5 == Y3:
        print('El vector ({0:.0f}, {1:.0f}) ya lo has ingresado.'
              .format(X5, Y5))
    if X5 == X4 and Y5 == Y4:
        print('El vector ({0:.0f}, {1:.0f}) ya lo has ingresado.'
              .format(X5, Y5))
    print(' ')

D1 = sqrt((X1-X2)**2 + (Y1-Y2)**2)
D2 = sqrt((X1-X3)**2 + (Y1-Y3)**2)
D3 = sqrt((X1-X4)**2 + (Y1-Y4)**2)
D4 = sqrt((X1-X5)**2 + (Y1-Y5)**2)
#"D1", "D2", "D3" y "D4" son las distancias de los 4 ultimos puntos al primero

cdt = D1
#"cdt" es la variable que determina quien es candidato a estar mas cerca

if cdt > D2:
   cdt = D2
    
if cdt > D3:
    cdt = D3
    
if cdt > D4:
    cdt = D4

if cdt == D1:
    print('El vector mas cercano es: ({0:.0f}, {1:.0f}).'.format(X2, Y2))
elif cdt == D2:
    print('El vector mas cercano es: ({0:.0f}, {1:.0f}).'.format(X3, Y3))
elif cdt == D3:
    print('El vector mas cercano es: ({0:.0f}, {1:.0f}).'.format(X4, Y4))
else:
    print('El vector mas cercano es: ({0:.0f}, {1:.0f}).'.format(X5, Y5))
