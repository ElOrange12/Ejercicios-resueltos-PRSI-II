##############################################################################
#                                                                            #
#Ej071.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:5 de noviembre del 2024                                               #
#                                                                            #
#Proposito:Este programa identifica entre mayúsculas y minúsculas.           #
#                                                                            #
##############################################################################

l = 0
#"l" es la letra que preguntamos
I = 0
#"I" son los intentos que tiene el usuario para poner una letra del albafeto

while I < 6:
    l = ord(input('Dime una letra del alfabeto: '))

    if l >= 65 and l <= 90:
        print('Es una MAYÚSCULA')
        I += 6

    elif l >= 97 and l <= 122:
        print('Es una MINÚSCULA')
        I += 6

    else:
        print('Eso no es una letra vuelve a intentarlo')
        print(' ')

        I += 1

print('Has fallado muchas veces, vuelve a iniciar el programa')
