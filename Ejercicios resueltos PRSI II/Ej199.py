##############################################################################
#                                                                            #
#Ej199.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:23 de marzo del 2025                                                  #
#                                                                            #
#Proposito:Este programa identigica si la cadena a contiene la cadena b.     #
#                                                                            #
##############################################################################
a = input("Introduce la cadena principal: ")
b = input("Introduce la cadena a buscar: ")

encontrado = False
len_a = len(a)
len_b = len(b)

# Recorremos la cadena principal
for i in range(len_a - len_b + 1):
    # Comparamos la subcadena de a con b
    if a[i:i+len_b] == b:
        encontrado = True
        break

if encontrado:
    print("La cadena b es una subcadena de a.")
else:
    print("La cadena b no es una subcadena de a.")
