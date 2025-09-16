##############################################################################
#                                                                            #
#Ej152.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:30 de enero del 2024                                                  #
#                                                                            #
#Proposito:Este programa identifica si una cadena tiene algún digito.        #
#                                                                            #
##############################################################################

#Primero pedimos una cadena al usuario.
cadena = input('Escribe cualquier cosa: ')

#Ahora necesitamos saber la longitud de la cadena.
L = len(cadena)

#Entonces hacemos un bucle para identificar si tiene algún digito o no.
a = 0

digitos = 0
for i in range(0, L)
     a = cadena[i]

     if a >= 48 and a <= 57:
         digitos += 1

if digitos == 0:
    print('No contiene dígitos')

else:
    print('Contiene dígitos')
