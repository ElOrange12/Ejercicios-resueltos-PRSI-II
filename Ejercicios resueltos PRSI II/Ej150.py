##############################################################################
#                                                                            #
#Ej150.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:30 de enero del 2024                                                  #
#                                                                            #
#Proposito:Este programa lee cuantos espacios en blanco tiene una cadena     #
#                                                                            #
##############################################################################

#Pedimos una cadena de caracteres que guardaremos en la variable "cadena".
cadena = input('Escribe una oración: ')

#Ahora necesitamos saber la longitud de la cadena.
L = len(cadena)

#Usando la longitud de la cadena, identificaremos los espacios en blanco.
a = 0

Eb = 0

for i in range(0, L):

    a = cadena[i]

    if a == ' ':

        Eb += 1

print('Esta cadena tiene {0} espacios en blanco.'.format(Eb))
