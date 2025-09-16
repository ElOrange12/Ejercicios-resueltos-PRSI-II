##############################################################################
#                                                                            #
#Ej60.py                                                                     #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:16 de mayo del 2024                                                   #
#                                                                            #
#Proposito:Un programa que identificara si un caracter es un "(" o ")"       #
#                                                                            #
##############################################################################
print('Este programa te preguntara un caracter y te dira si es un paréntesis')

C = input('Dime un caracter: ')
#"C" Es el caracter que nos preguntan

if ord(C) == 40 or ord(C) == 41:
    print('Es paréntesis')
