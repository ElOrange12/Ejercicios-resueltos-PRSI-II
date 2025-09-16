##############################################################################
#                                                                            #
#Ej159.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:31 de enero del 2025                                                  #
#                                                                            #
#Proposito:Este programa identifica si hay alguna letra de la longitud que   #
#          indique el usuario.                                               #
#                                                                            #
##############################################################################
#Pedimos la cadena y el número.
cadena = input('Escribe una frase: ')
numero = int(input('Escribe un número: '))

#Contamos la longitud de la cadena.
L = len(cadena)

#Contamos las palabras para saber si hay alguna mas larga o igual que el 
#número indicado.

a = 0
CL = 0
#"CL" es el contador de letras.
CP = 0
#"CP" es el contador de letras que tienen las letras iguales o mas largas al 
#número pedido.

for i in range(0, L):

    a = cadena[i]

    #Esta parte identifica cuando acaban las palabras.
    if a == ' ':
        CL = 0

    elif a == '.':
        CL = 0

    elif a == ',':
        CL = 0
    
    #Aqui te cuentan las letras que tienen las palabras.
    else:
        CL += 1

        #Este if identifica si hay alguna palabras mas larga o igual al número
        #dado
        if CL == numero:
            CP += 1

#Este print muestra si hay alguna palabra mas larga o igual al número de
#palabras indicado.
if CP == 0:
    print('No hay ninguna palabra mas larga o igual a {0:.0f} letras.'
          .format(numero))
    
else:
    print('Hay alguna palabra mas larga o igual a {0:.0f} letras.'
          .format(numero))
