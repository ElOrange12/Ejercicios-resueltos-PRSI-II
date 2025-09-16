##############################################################################
#                                                                            #
#Ej059.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:15 de mayo del 2024                                                   #
#                                                                            #
#Proposito:Un programa que te dice entre dos personas quien es mas joven     #
#                                                                            #
##############################################################################
print('Dime las edades de dos personas y te dire cual es mayor')

P1 = float(input('Dime la edad de la primera persona: '))
#"P1" la edad de la primera persona
P2 = float(input('Dime la edad de la segunda persona: '))
#"P2" la edad de la segunda persona

if P1 == P2:
    print('Tienen la misma edad')

else:
    if P1 < P2:
        print('La primera persona es mas joven')

    if P1 > P2:
        print('La segunda persona es mas joven')
