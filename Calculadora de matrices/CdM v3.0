##############################################################################
#                                                                            #
#CdM v3.0.py                                                                 #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:28 de marzo del 2024                                                  #
#                                                                            #
#Proposito:Este programa calcula operaciones con matrices.                   #
#                                                                            #
##############################################################################

#Se presenta el programa.
print('Bienvenido a la calculadora de matrices')
print(' ')

R = 'S'
#Este bucle es el encargado de seguir con el programa si el usuario quiere.
while R == 'S':

    #Preguntamos que operacion quiere hacer.
    O = 0
    #Este bucle comprueba que se conteste una respuesta correcta.
    while O < 1 or O > 5:
        print('Que operación o operaciones quieres realizar:')
        print('1 --> Suma de matrices.')
        print('2 --> Resta de matrices.')
        print('3 --> Multiplicación de matrices. (Work in progress)')
        print('4 --> Determinante de una matriz. (Work in progress)')
        print('5 --> Cerrar. ')
        print('')

        O = int(input('¿Qué quieres hacer?: '))
        print('')

        #Esta condición identifica cuando la respuesta no es posible.
        if O < 1 or O > 5:
            print('Esa no es un acción posible')
            print('')
        #Esta condición hace que al poner "5" se termina el programa.
        elif O == 5:
            R = 'N'
    
    #Suma de matrices.
    if O == 1:
        print('Para sumar matrices necesitaremos dos matrices y estan deben'
              ' ser iguales, es decir, mismas filas y columnas.')
        print('')
        
        FS = int(input('¿Cuantas filas tienen las matrices?: '))
        CS = int(input('¿Cuantas columnas tienen las matrices?: '))
        print('')

        #Creamos la primera matriz
        print('----> Introduce la primera matriz')
        M1 = []

        #Ahora preguntamos la matriz
        for i in range(FS):
            M1.append([0] * CS)

        for j in range(FS):
            for k in range(CS):
                M1[j][k] = float(input('Dime el número que esta en F{0:.0f} '
                                       'C{1:.0f}: '.format(j+1, k+1)))
        print('')

        #Creamos la segunda matriz
        print('----> Introduce la segunda matriz')
        M2 = []

        #Ahora preguntamos la matriz
        for i in range(FS):
            M2.append([0] * CS)

        for j in range(FS):
            for k in range(CS):
                M2[j][k] = float(input('Dime el número que esta en F{0:.0f} '
                                       'C{1:.0f}: '.format(j+1, k+1)))
        print('')

        #Creamos la matriz resultante
        MT = []

        #Ahora calculamos la matriz resultante
        for i in range(FS):
            MT.append([0] * CS)

        for j in range(FS):
            for k in range(CS):
                MT[j][k] = M1[j][k] + M2[j][k]
        
        #Ahora la mostramos en pantalla
        for i in range(FS):
            print(MT[i])

    #Resta de matrices.
    elif O == 2:
        print('Para restar matrices necesitaremos dos matrices y estan deben'
              ' ser iguales, es decir, mismas filas y columnas.')
        print('')
        
        #Pedimos filas y columnas de las dos matrices que restaremos.
        FR = int(input('¿Cuantas filas tienen las matrices?: '))
        CR = int(input('¿Cuantas columnas tienen las matrices?: '))
        print('')

        #Creamos la primera matriz.
        print('----> Introduce la primera matriz')
        M1 = []

        #Ahora preguntamos la primera matriz.
        for i in range(FR):
            M1.append([0] * CR)

        for j in range(FR):
            for k in range(CR):
                M1[j][k] = float(input('Dime el número que esta en F{0:.0f} '
                                       'C{1:.0f}: '.format(j+1, k+1)))
        print('')

        #Creamos la segunda matriz.
        print('----> Introduce la segunda matriz')
        M2 = []

        #Ahora preguntamos la segunda matriz.
        for i in range(FR):
            M2.append([0] * CR)

        for j in range(FR):
            for k in range(CR):
                M2[j][k] = float(input('Dime el número que esta en F{0:.0f} '
                                       'C{1:.0f}: '.format(j+1, k+1)))
        print('')

        #Creamos la matriz resultante.
        MT = []

        #Ahora calculamos la matriz resultante.
        for i in range(FR):
            MT.append([0] * CR)

        for j in range(FR):
            for k in range(CR):
                MT[j][k] = M1[j][k] - M2[j][k]
        
        #Ahora la mostramos en pantalla.
        for i in range(FR):
            print(MT[i])

    #Multiplicación de matrices.
    elif O == 3:
        print('Esta función esta aun en proceso no es posible ejecutarla.')
        print('')

    #Determinante de una matriz.
    elif O == 4:
        print('Esta función esta aun en proceso no es posible ejecutarla.')
        print('')

    #Preguntamos la opción de seguir operando con la calculadora o cerar el 
    #programa.
    if R == 'S':           
        print('¿Quieres seguir operando?')
        R = input('para seguir escribe "S" y para terminar "N": ')
