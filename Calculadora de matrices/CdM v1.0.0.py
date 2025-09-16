##############################################################################
#                                                                            #
#CdM v1.0.0.py                                                                      #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:7 de noviembre del 2024                                               #
#                                                                            #
#Proposito:Un programa que calcule los determinantes de matrices de          #
#          cualquier orden.                                                  #
#                                                                            #
##############################################################################

print('Bienvenido a la calculadora de determinates de matrices, esta calculad'
      'ora halla el valor de determinantes de matrices de Orden 2,3 y 4.')
print(' ')
print('Recuerda que para calcular el determinante la matriz debe ser cuadrada'
      ', es decir que tenga el mismo numero de filas que de columnas.')
print(' ')

Rsta = 'S'
#"Rsta" es la respuesta para saber si el usuario quiere seguir operando o no.

while Rsta != 'N':

    Ord = int(input('De que orden es tu matriz: '))
    #"Ord" es el valor del orden de la matriz dicha.
    print(' ')

    print('A continuación dime los numeros de tu matriz de izquierda a derech'
          'a siendo el primer numero de la primera fila a11 el segundo a12...'
          ' y el primero de la segundo fila seria a21 y el segundo a22...')
    print(' ')

    C = 0
    #"C" es el contador de columnas
    F = 0
    #"F" es el contador de filas
  
    if Ord == 1:
        print('Esto no es una matriz es un número.')
        print(' ')

    elif Ord == 2:
            
        a11 = float(input('Dime a11: '))
        a12 = float(input('Dime a12: '))
        a21 = float(input('Dime a21: '))
        a22 = float(input('Dime a22: '))

        DetA = int(a11*a22 - a12*a21)

        print('El determinante de tu matriz de orden {0} es {1}.'
              .format(Ord, DetA))
        print(' ')

    elif Ord == 3:

        a11 = float(input('Dime a11: '))
        a12 = float(input('Dime a12: '))
        a13 = float(input('Dime a13: '))
        a21 = float(input('Dime a21: '))
        a22 = float(input('Dime a22: '))
        a23 = float(input('Dime a23: '))
        a31 = float(input('Dime a31: '))
        a32 = float(input('Dime a32: '))
        a33 = float(input('Dime a33: '))

        DetA = int(a11*a22*a33 + a21*a32*a13 + a12*a23*a31 - a13*a22*a31 - 
                a12*a21*a33 - a11*a23*a32)

        print('El determinante de tu matriz de orden {0} es {1}.'
              .format(Ord, DetA))
        print(' ')
        
    elif Ord == 4:

        a11 = float(input('Dime a11: '))
        a12 = float(input('Dime a12: '))
        a13 = float(input('Dime a13: '))
        a14 = float(input('Dime a14: '))
        a21 = float(input('Dime a21: '))
        a22 = float(input('Dime a22: '))
        a23 = float(input('Dime a23: '))
        a24 = float(input('Dime a24: '))
        a31 = float(input('Dime a31: '))
        a32 = float(input('Dime a32: '))
        a33 = float(input('Dime a33: '))
        a34 = float(input('Dime a34: '))
        a41 = float(input('Dime a41: '))
        a42 = float(input('Dime a42: '))
        a43 = float(input('Dime a43: '))
        a44 = float(input('Dime a44: '))

        A11 = (a22*a33*a44 + a24*a32*a43 + a23*a34*a42 - a24*a33*a42
                 - a23*a32*a44 - a22*a34*a43)
        A21 = (-1)*(a12*a33*a44 + a14*a32*a43 + a13*a34*a42 - a14*a33*a42
                 - a13*a32*a44 - a12*a34*a43)
        A31 = (a12*a23*a44 + a14*a22*a43 + a13*a24*a42 - a14*a23*a42
                 - a13*a22*a44 - a12*a24*a43)
        A41 = (-1)*(a12*a23*a34 + a14*a22*a33 + a13*a24*a32 - a14*a23*a32
                 - a13*a22*a34 - a12*a24*a33)
        
        DetA = int(a11*A11 + a21*A21 + a31*A31 + a41*A41)

        print('El determinante de tu matriz de orden {0} es {1}.'
              .format(Ord, DetA))
        print(' ')

    else:

        print('No puedo hacer matrices tan grandes')
        print(' ')

    print('¿Quieres seguir haciendo determinantes?')
    Rsta = input('"S" si es sí y "N" si es no: ')
    print(' ')

print('Hasta pronto.')
print(' ')
