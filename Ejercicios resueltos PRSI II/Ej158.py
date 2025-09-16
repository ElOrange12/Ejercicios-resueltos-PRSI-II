##############################################################################
#                                                                            #
#Ej158.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:31 de enero del 2025                                                  #
#                                                                            #
#Proposito:Este programa lee una cadena y un número y identifica cuantas     #
#          palabras tiene ese número de letras.                              #
#                                                                            #
##############################################################################

#Pedimos la cadena y el número.
cadena = input('Escribe una frase: ')
numero = int(input('Escribe un número: '))

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
        if CL == numero:
            CP += 1

        elif CL == numero + 1:
            CP -= 1

#Este print muestra cuantas palabras ahi con el número de palabras indicado.
print('Hay {0:.0f} palabras con la logitud de {1:.0f} letras.'
      .format(CP, numero))
