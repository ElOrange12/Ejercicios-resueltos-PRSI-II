##############################################################################
#                                                                            #
#Ej160.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:31 de enero del 2025                                                  #
#                                                                            #
#Proposito:Este programa identifica si todos las palabras de una cadena      #
#          tienen la longitud del numeros de letras indicado.                #
#                                                                            #
##############################################################################

#Pedimos una cadena al usuario.
cadena = input('Escribe una frase: ')

#Contamos las palabras que tiene la cadena.
cambios = 0
anterior = ' '

for carácter in cadena:
    if carácter == ' ' and anterior != ' ':
        cambios += 1
    anterior = carácter
    
if cadena[-1] == ' ':
    cambios -= 1

palabras = cambios + 1

#Ahora le pedimos un número al usuario.
número = int(input('Dime un número: '))

#Hallamos la longitud de la cadena.
L = len(cadena)

#Ahora con la longitud de la cadena vamos contando cuantas letras tiene cada
#palabra.

a = 0
CL = 0
#"CL" es el contador de letras.
CP = 0
#"CP" es el contador de letras que tienen las letras iguales al número pedido.

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

        #Este if cuenta cuantas palabras hay con el número de palabras
        #indicado por el usuario.
        if CL == número:
            CP += 1

        elif CL == número + 1:
            CP -= 1

if palabras == CP:
    print('Todas las palabras de la oración tiene la longitud de {0:.0f} '
          'letras.'.format(número))
    
else:
    print('No todas las palabras de la oración tiene la longitud de {0:.0f} '
          'letras.'.format(número))
