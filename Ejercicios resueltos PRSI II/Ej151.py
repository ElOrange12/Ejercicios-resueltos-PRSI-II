##############################################################################
#                                                                            #
#Ej151.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:30 de enero del 2024                                                  #
#                                                                            #
#Proposito:Este programa identifica cuantas mayúsculas tiene un cadena.      #
#                                                                            #
##############################################################################

#Primero pedimos una cadena al usuario.
cadena = input('Escribe una oración: ')

#Ahora necesitamos saber la longitud de la cadena.
L = len(cadena)

#Entonces hacemos un bucle para identificar cuantas mayúsculas tiene la 
#cadena.
a = 0

mayusculas = 0
for i in range(0, L):
    a = ord(cadena[i])

    if a >= 65 and a <= 90:
        mayusculas += 1

print('La cadena tiene {0} mayusculas.'.format(mayusculas))
