##############################################################################
#                                                                            #
#Ej115.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:6 de mayo del 2024                                                    #
#                                                                            #
#Proposito:Un programa que es una calculadora de matrices                    #
#                                                                            #
##############################################################################
from math import acos, pi, sqrt

print('Bienvenido a la calculara de vectores, esta calculadora hace operacion'
      'es con dos vector que introduzcas tu')

opcion = ''

print('Escribe el primer vector')

XV1 = int(input('Dime su componente x: '))
YV1 = int(input('Dime su componente y: '))
ZV1 = int(input('Dime su componente z: '))
#"XV1", "YV1" y "ZV1" son las componentes del vector.

V1 = '({0}, {1}, {2})'.format(XV1, YV1, ZV1)
#"V1" es el primer vector

print('Escribe el segundo vector')

XV2 = int(input('Dime su componente x: '))
YV2 = int(input('Dime su componente y: '))
ZV2 = int(input('Dime su componente z: '))
#"XV2", "YV2" y "ZV2" son las componentes del vector.

V2 = '({0}, {1}, {2})'.format(XV2, YV2, ZV2)
#"V2" es el primer vector

while opcion != '9':

    while opcion < '1' or opcion > '9':

        #Menu de la calculadora
        print('Escoge una opcion')
        print('1) Cambiar el primer vector  ')
        print('2) Cambiar el segundo vector')
        print('3) Calcular la suma')
        print('4) Calcular la diferencia')
        print('5) Calcular el producto escalar')
        print('6) Calcular el producto vectorial')
        print('7) Calcular el ángulo (en grados) entre ellos')
        print('8) Calcular la longitud')
        print('9) Finalizar')

        opcion = input('Teclea el número de la opcion y pulsa el enter: ')

        if opcion < '1' or opcion > '9':
            print('Solo hay nueve opciones: 1, 2, 3, 4, 5, 6, 7, 8 o 9. Tú has'
                  ' tecleado', opcion)

    if opcion == '1':

        #Cambiar el primer vector
        XV1 = int(input('Dime su componente x: '))
        YV1 = int(input('Dime su componente y: '))
        ZV1 = int(input('Dime su componente z: '))

        print('el primer vector es ({0}, {1}, {2})'.format(XV1, YV1, ZV1))

    elif opcion == '2':

        #Cambiar el segundo vector
        XV2 = int(input('Dime su componente x: '))
        YV2 = int(input('Dime su componente y: '))
        ZV2 = int(input('Dime su componente z: '))

        print('el segundo vector es ({0}, {1}, {2})'.format(XV2, YV2, ZV2))

    elif opcion == '3':

        #Suma de vectores
        SumaX = XV1 + XV2
        SumaY = YV1 + YV2
        SumaZ = ZV1 + ZV2

        print('La suma de los vectores: V1{0} y V2{1}, es el vector: ({2},' 
              ' {3}, {4})'.format(V1, V2, SumaX, SumaY, SumaZ))
        
    elif opcion == '4':

        #Resta de vectores
        RestaX = XV1 - XV2
        RestaY = YV1 - YV2
        RestaZ = ZV1 - ZV2

        print('La resta de los vectores: V1{0} y V2{1}, es el vector: ({2},' 
              ' {3}, {4})'.format(V1, V2, RestaX, RestaY, RestaZ))
        
    elif opcion == '5':

        #Producto Escalar de los vectores
        ProdEsc = XV1*XV2 + YV1*YV2 + ZV1*ZV2

        print('El producto escalar de los vectores: V1{0} y V2{1}, es {2}'
               .format(V1, V2, ProdEsc))
        
    elif opcion == '6':

        #Producto Vectorial de los vectores
        PVX = YV1*ZV2 - YV2*ZV1
        PVY = XV2*ZV1 - XV1*ZV2
        PVZ = XV1*YV2 - XV2*YV1

        print('El producto vectorial de los vectores: V1{0} y V2{1}, es el ve'
              'ctor: ({2}, {3}, {4})'.format(V1, V2, PVX, PVY, PVZ))
        
    elif opcion == '7':

        #Ángulo que forman los dos vectores
        alfa = int(180/pi * acos((XV1*XV2 + YV1*YV2 + ZV1*ZV2)/(sqrt((XV1**2
               + YV1**2 + ZV1**2) * (XV2**2 + YV2**2 + ZV2**2)))))
        
        print('El ángulo de los vectores: V1{0} y V2{1}, es {2}'.format(V1, 
               V2, alfa))

    elif opcion == '8':

        #Longitud de uno de los vectores

        VS = 0
        #"VS" es vector seleccionado

        while VS != '1' and VS != '2':
            VS = input('¿De que vector quieres saber la longitud 1 o 2?: ')

            if VS == '1':
                
                LV = sqrt(XV1**2 + YV1**2 + ZV1**2)
                #"LV" es la longitud del vector selecionado

                print('La longitud del vector: {0}, es {1:.2f}'.format(V1, 
                       LV))

            elif VS == '2':

                LV = sqrt(XV2**2 + YV2**2 + ZV2**2)

                print('La longitud del vector: {0}, es {1:.2f}'.format(V2, 
                       LV))
            
            else:
                print('Solo hay dos opciones 1 o 2')

    if opcion != '9':
        print('¿Qué quieres hacer ahora?')
        opcion = ''

print('Gracias por usar nuestra calculadora')
