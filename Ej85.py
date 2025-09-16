##############################################################################
#                                                                            #
#Ej85.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:21 de noviembre del 2024                                              #
#                                                                            #
#Proposito:Este programa determina el valor de la nota introducida.          #
#                                                                            #
##############################################################################

print('A continuacíon deberás introducir la nota del examen y la clasificare '
      'como Suspendida, Aprobado, Notable, Sobresaliente o Matricula.')
print('El valor de nota debera sera mayor o igual que 0 y menor o igual que 1'
      '0.')
print(' ')

Rst = 'N'
#"Rst" es la variable que determina si el usuario quiere seguir introduciendo 
#notas.

while Rst != 'S':

    N = -1
    #"N" es la variable de la Nota del examen.

    while N < 0 or N > 10:
        N = float(input('Dime la nota del examen: '))
        print(' ')
        if N < 0:
            print('La nota no puede ser negativa.')
            print(' ')
        elif N > 10:
            print('La nota no puede ser mas alta que 10.')
            print(' ')

    if N < 5:
        print('Este examen es un suspenso.')
        print(' ')
    elif N >= 5 and N < 7:
        print('Este examen es un aprobado.')
        print(' ')
    elif N >= 7 and N < 9:
        print('Este examen es un notable.')
        print(' ')
    elif N >= 9 and N < 10:
        print('Este examen es un sobresaliente.')
        print(' ')
    else:
        print('Este examen es una matricula de honor.')
        print(' ')

    print('¿Quieres poner otro examen?')
    Rst = input('Escribe "S" si es si y "N" si es que no.')
    print(' ')
