##############################################################################
#                                                                            #
#Ej040.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:29 de mato del 2024                                                   #
#                                                                            #
#Proposito: Calcula la tasa de interes                                       #
#                                                                            #
##############################################################################

print('Calcularemos la tasa de interes que tenga tu capital con el porcentaje'
      ' y años que digas')

C = float(input('Dime la cantidad de euros que quieres ingresar: '))

x = float(input('Dime el porcentaje de interes anual: '))

n = float(input('Dime los años que estará: '))

TdI = C * (1 + x/100)**n

print('Tu capital se a convertido en {0:.2f}€'.format(TdI))
