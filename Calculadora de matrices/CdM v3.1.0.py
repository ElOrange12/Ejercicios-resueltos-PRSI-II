##############################################################################
#                                                                            #
#CdM v3.1.0.py                                                               #
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
    while O < 1 or O > 6:
        print('Que operación o operaciones quieres realizar:')
        print('1 --> Suma de matrices.')
        print('2 --> Resta de matrices.')
        print('3 --> Multiplicación de matrices.')
        print('4 --> Determinante de una matriz, de grado 2 o 3.')
        print('5 --> Inversa de una matriz, de grado 2 o 3.')
        print('6 --> Cerrar. ')
        print('')

        O = int(input('¿Qué quieres hacer?: '))
        print('')

        #Esta condición identifica cuando la respuesta no es posible.
        if O < 1 or O > 6:
            print('Esa no es un acción posible')
            print('')
        #Esta condición hace que al poner "5" se termina el programa.
        elif O == 6:
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
            print('')

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
            print('')

    #Multiplicación de matrices.
    elif O == 3:
        print('Para multiplicar matrices deberemos tener dos matrices, de las'
              ' cuales deberan ser iguales las columnas de la primera y las' 
              ' filas de la segunda.')
        print('')

        #Pedimos filas y columnas de las matrices y comprobamos que sean 
        #iguales las columnas de la primera y las filas de la segunda.
        C1 = 0
        F2 = 1
        while C1 != F2:

            #Pedimos las filas y columnas de la primera matriz.
            F1 = int(input('Dime las filas de la primera matriz: '))
            C1 = int(input('Dime las columnas de la primera matriz: '))
            print('')

            #Pedimos las filas y columnas de la primera matriz.
            F2 = int(input('Dime las filas de la segunda matriz: '))
            C2 = int(input('Dime las columnas de la segunda matriz: '))
            print('')

            if C1 != F2:
                print('No se podría multiplicar, las filas de la primera y las'
                      ' columnas de la segunda no son iguales.')
                print('')

        #Creamos la primera matriz.
        print('----> Introduce la primera matriz')
        M1 = []

        #Ahora preguntamos la primera matriz.
        for i in range(F1):
            M1.append([0] * C1)

        for j in range(F1):
            for k in range(C1):
                M1[j][k] = float(input('Dime el número que esta en F{0:.0f} '
                                       'C{1:.0f}: '.format(j+1, k+1)))
        print('')

        #Creamos la segunda matriz.
        print('----> Introduce la segunda matriz')
        M2 = []

        #Ahora preguntamos la segunda matriz.
        for i in range(F2):
            M2.append([0] * C2)

        for j in range(F2):
            for k in range(C2):
                M2[j][k] = float(input('Dime el número que esta en F{0:.0f} '
                                       'C{1:.0f}: '.format(j+1, k+1)))
        print('')

        #Creamos la matriz resultante.
        MT = []

        #Hayamos la matriz resultante.
        for i in range(F1):
            M2.append([0] * C2)

        for j in range(F1):
            for k in range(C2):
                for l in range(C1):
                    MT[j][k] += M1[j][l] + M2[l][k]

        #Ahora la mostramos en pantalla.
        for i in range(F1):
            print(MT[i])
            print('')
    
    #Determinante de una matriz.
    elif O == 4:
        print('Para calcular el determinante de una matriz necesitaremos que '
              ' sea cuadrada, es decir filas iguales a las columnas.')
        print('')

        #Pedimos las filas y columnas de la matriz.
        FD = 0
        CD = 1

        while FD != CD or FD <= 0 or FD >= 4:
            FD = int(input('Dime el número de filas que tiene la matriz: '))
            CD = int(input('Dime el número de columnas que tiene la matriz: '
                           ''))
            print('')

            if FD != CD:
                print('La matriz debe ser cuadrada.')
                print('')

            elif FD == 0:
                print('Una matriz de orden 0, no existe.')
                print('')

            elif FD < 0:
                print('La matriz no puede tener filas o columnas negativas.')
                print('')

            elif FD >= 4:
                print('Esta calculadora no hace determinantes mayores a orden'
                      ' 3.')
                print('')

        #Creamos la matriz.
        print('----> Introduce la matriz')
        M = []

        #Ahora preguntamos la matriz.
        for i in range(FD):
            M.append([0] * CD)

        for j in range(FD):
            for k in range(CD):
                M[j][k] = float(input('Dime el número que esta en F{0:.0f} '
                                       'C{1:.0f}: '.format(j+1, k+1)))
        print('')

        #Calculamos el determinante
        Det = 0

        if FD == 2:
            Det = M[0][0]*M[1][1] - M[0][1]*M[1][0]

        elif FD == 3:
            Det = ((M[0][0]*M[1][1]*M[2][2]) + (M[1][0]*M[2][1]*M[0][2]) + 
                   (M[0][1]*M[1][2]*M[2][0]) - (M[0][2]*M[1][1]*M[2][0]) - 
                   (M[1][2]*M[2][1]*M[0][0]) - (M[0][1]*M[1][0]*M[2][2]))

        #Lo mostramos por pantalla    
        print('El determinante de la matriz es {0:.0f}'.format(Det))
        print('')
                
    elif O == 5:
        print('Para hacer la inversa de una matriz necesitaremos que sea '
              'cuadrada, es decir filas iguales a las columnas.')
        print('')

        #Pedimos las filas y columnas de la matriz.
        FI = 0
        CI = 1

        while FI != CI or FI <= 0 or FI >= 4:
            FI = int(input('Dime el número de filas que tiene la matriz: '))
            CI = int(input('Dime el número de columnas que tiene la matriz: '
                           ''))
            print('')

            if FI != CI:
                print('La matriz debe ser cuadrada.')
                print('')

            elif FI == 0:
                print('Una matriz de orden 0, no existe.')
                print('')

            elif FI < 0:
                print('La matriz no puede tener filas o columnas negativas.')
                print('')

            elif FI >= 4:
                print('Esta calculadora no hace inversas mayores a orden 3.')
                print('')

        #Creamos la matriz.
        print('----> Introduce la matriz')
        M = []

        #Ahora preguntamos la matriz.
        for i in range(FI):
            M.append([0] * CI)

        for j in range(FI):
            for k in range(CI):
                M[j][k] = float(input('Dime el número que esta en F{0:.0f} '
                                       'C{1:.0f}: '.format(j+1, k+1)))
        print('')  

        #En caso de ser un matriz de orden 2.
        if FI == 2:

            #Calculamos el determinante.
            Det2 = M[0][0]*M[1][1] - M[0][1]*M[1][0]

            #Creamos la matriz adjunta.
            MA = []

            for i in range(FI):
                MA.append([0] * CI)

            MA[0][0] = M[1][1]
            MA[0][1] = -M[1][0]
            MA[1][0] = -M[0][1]
            MA[1][1] = M[0][0]

            #Hacemos la matriz adjunta transversa.
            MAt = []

            for i in range(FI):
                MAt.append([0] * CI)

            for j in range(FI):
                for k in range(CI):

                    MAt[j][k] =  MA[k][j]

            #Ahora calculamos la inversa
            MI = []

            for i in range(FI):
                MI.append([0] * CI)

            for j in range(FI):
                for k in range(CI):

                    MI[j][k] = (MAt[j][k] / Det2)

            #La mostramos por pantalla    
            for i in range(FI):
                print(MI[i])
                print('')

        #En caso de ser una matriz de orden 3.
        if FI == 3:

            #Calculamos el determinante.
            Det3 = ((M[0][0]*M[1][1]*M[2][2]) + (M[1][0]*M[2][1]*M[0][2]) + 
                   (M[0][1]*M[1][2]*M[2][0]) - (M[0][2]*M[1][1]*M[2][0]) -
                   (M[1][2]*M[2][1]*M[0][0]) - (M[0][1]*M[1][0]*M[2][2]))
            
            #Calculamos sus adjuntos.
            MA = []

            for i in range(FI):
                MA.append([0] * CI)

            MA[0][0] = (M[1][1]*M[2][2] - M[1][2]*M[2][1])
            MA[0][1] = -(M[1][0]*M[2][2] - M[1][2]*M[2][0])
            MA[0][2] = (M[1][0]*M[2][1] - M[1][1]*M[2][0])
            MA[1][0] = -(M[0][1]*M[2][2] - M[0][2]*M[2][1])
            MA[1][1] = (M[0][0]*M[2][2] - M[0][2]*M[2][0])
            MA[1][2] = -(M[0][0]*M[2][1] - M[0][1]*M[2][0])
            MA[2][0] = (M[0][1]*M[1][2] - M[0][2]*M[1][1])
            MA[2][1] = -(M[0][0]*M[1][2] - M[0][2]*M[1][0])
            MA[2][2] = (M[0][0]*M[1][1] - M[0][1]*M[1][0])

            #Hayamos su adjunta transpuesta
            MAt = []

            for i in range(FI):
                MAt.append([0] * CI)
            
            for j in range(FI):
                for k in range(CI):

                    MAt[j][k] = MA[k][j]

            #Calculamos su inversa.
            MI = []

            for i in range(FI):
                MI.append([0] * CI)

            for j in range(FI):
                for k in range(CI):

                    MI[j][k] = (MAt[j][k] / Det3)

            #La mostramos por pantalla    
            for i in range(FI):
                print(MI[i])
                print('')

    #Preguntamos la opción de seguir operando con la calculadora o cerar el 
    #programa.
    if R == 'S':           
        print('¿Quieres seguir operando?')
        R = input('para seguir escribe "S" y para terminar "N": ')
        print('')
