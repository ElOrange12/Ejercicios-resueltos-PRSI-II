##############################################################################
#                                                                            #
#Ej130.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:22 de noviembre del 2024                                              #
#                                                                            #
#Proposito:Este programa calcula el maximo común multiplo de tres números    #
#          dados.                                                            #
#                                                                            #
##############################################################################

print('A continuación te pedire tres números enteros positivos distintos y te'
      ' dire su máximo común divisor.')
print(' ')

n1 = -1
n2 = -1
n3 = -1

#Comprobar si los números son positivos
while n1 < 0 and n2 < 0 and n3 < 0:

    n1 = float(input('Dime el 1º número: '))
    n2 = float(input('Dime el 2º número: '))
    n3 = float(input('Dime el 3º número: '))

    if n1 < 0 and n2 < 0 and n3 < 0:
        print('Todos los números son negativos')

    else:
        if n1 < 0 and n2 < 0:
            print('Los números {0:.0f} y {1.0f} son negativos.'.format(n1, n2))

        elif n1 < 0 and n3 < 0:
            print('Los números {0:.0f} y {1.0f} son negativos.'.format(n1, n3))

        elif n2 < 0 and n3 < 0:
            print('Los números {0:.0f} y {1.0f} son negativos.'.format(n2, n3))

        else:
            if n1 < 0:
                print('El número {0:.0f} es negativo.'.format(n1))

            elif n2 < 0:
                print('El número {0:.0f} es negativo.'.format(n2))

            elif n3 < 0:
                print('El número {0:.0f} es negativo.'.format(n3))

#Ordenarlos de mayor a menor siendo a el mas grande y c el mas pequeño
a = n1
if a < n2:
    a = n2
if a < n3:
    a = n3

c = n1
if c > n2:
    c = n2
if c > n3:
    c = n3

b = n1
if a == n1:
    if c == n3:
        b = n2
    elif c == n2:
        b = n3
elif a == n2:
    if c == n3:
        b = n1
    elif c == n1:
        b = n3
elif a == n3:
    if c == n2:
        b = n1
    elif c == n1:
        b = n2

#Sacamos el maximo común divisor de los dos más pequeños.

mod1 = 1
#"mod1" es el modulo de la división de los dos números más pequeños.

while mod1 != 0:
    mod1 = b % c

    if mod1 != 0:
        b = c
        c = mod1
    elif mod1 == 0:
        mcd1 = c

#Sacamos el máximo común divisor de el mas alto y el mcd de los dos 
#anteriores.

mod2 = 1
#"mod2" es el modulo de la división entre el número mas alto y el mcd de los 
#dos anteriores.

while mod2 != 0:
    mod2 = a % mcd1

    if mod2 != 0:
        a = mcd1
        mcd1 = mod2
    elif mod1 == 0:
        mcd2 = mcd1

print('El máximo común divisor de {0:.0f}, {1:.0f} y {2:.0f} es: {3:.0f}.'
      .format(n1, n2, n3, mcd2))
