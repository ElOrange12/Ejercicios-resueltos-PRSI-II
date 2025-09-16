##############################################################################
#                                                                            #
#Ej147.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:16 de enero del 2025                                                  #
#                                                                            #
#Proposito:Este programa te dice la letra del DNI con solo saber los números.#
#                                                                            #
##############################################################################

NDNI = int(input('Dime el número de un DNI: '))
#"NDNI" es el número del DNI.
Letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
#Orden de las letras del DNI.
LN = NDNI % 23
#"LN" es el resto de el total de la suma de los números.
L = Letras[LN]
print('La letra del DNI es {0}.'.format(L))
