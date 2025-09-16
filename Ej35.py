##############################################################################
#                                                                            #
#Ej35.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:30 de abril del 2024                                                  #
#                                                                            #
#Proposito:Un programa que calcule el perimetro y área de un cuadrado        #
#                                                                            #
##############################################################################

l = float(input('Introduce el lado del cuadrado: '))
#"l" es el lado del cuadrado

p = l * 4
#"p" es el perimetro del cuadrado
a = l * l
#"a" es el área del cuadrado
print('El perimetro del cuadrado de lado {0} es {1} y el area es {2:.2f}'
      .format(l, p, a))
