##############################################################################
#                                                                            #
#Ej188.py                                                                    #
#                                                                            #
#Autor:Daniel Oliveira Vidal                                                 #
#                                                                            #
#Fecha:25 de febrero del 2025                                                #
#                                                                            #
#Proposito:Este progama encripta mensajes.                                   #
#                                                                            #
##############################################################################

#Guardamos las letras y los números en variables.
LETRAS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
letras = 'abcdefghijklmnñopqrstuvwxyz'
Números = '0123456789'

#Pedimos una cadena la cual transcribir.
mensaje = input('Díme una cadena la cual transcribir: ')
#Pedimos el número "n" de la criptación.
n = int(input('Díme el número de encriptamiento de tu mensaje: '))

#Inicializamos una variable vacia para concatenar el resultado.
cadena_saliente = ''

#Ahora analizaremos los carácteres que hay en la cadena.
for carácter in mensaje:

    #Aquí se cambiaran los caracteres n veces lo que se haya indicado.
    L = 0

    #Guardamos el valor en la tabla ASCII del número.
    OrdC = ord(carácter)
        
    #Identificamos aquí si el carácter es una mayuscula.
    if OrdC >= 65 and OrdC <= 90 or OrdC == 209:
            
        #Guardamos la longitud de la cadena donde estan almacenadas las letras
        #mayúsculas.
        L = len(LETRAS)

        #Identificamos que letra és.
        for i in range(0, L):
                
            a = LETRAS[i]
            
            if carácter == a:
                LETRA = i
            
        #Aqui aplicamos el número "n" de encriptamiento.
        Lugar = LETRA + n

        #Si el número es mayor que la longitud de la cadena este "if" hará la
        #equivalencia como si volviera a contar desde el inicio.
        if Lugar >= 27:
            while Lugar >= 27:
                Lugar = 27 - Lugar

            cadena_saliente = cadena_saliente + LETRAS[Lugar]
            
        #Aquí se añade la letra a la "cadena_saliente".
        else:
            cadena_saliente = cadena_saliente + LETRAS[Lugar]

    #Identificamos si el caracter es minúscula
    elif OrdC >= 97 and OrdC <= 122 or OrdC == 241:

        #Guardamos la longitud de la cadena donde estan almacenadas las letras
        #minúsculas.
        L = len(letras)

        #Identificamos que letra és.
        for i in range(0, L):
                
            a = letras[i]
            
            if carácter == a:
                letra = i
            
        #Aqui aplicamos el número "n" de encriptamiento.
        Lugar = letra + n

        #Si el número es mayor que la longitud de la cadena este "if" hará la
        #equivalencia como si volviera a contar desde el inicio.
        if Lugar >= 27:
            while Lugar >= 27:
                Lugar = 27 - Lugar

            cadena_saliente = cadena_saliente + letras[Lugar]
            
        #Aquí se añade la letra a la "cadena_saliente".
        else:
            cadena_saliente = cadena_saliente + letras[Lugar]

    elif OrdC >= 48 and OrdC <= 57:

        #Guardamos la longitud de la cadena donde estan almacenadas las letras
        #mayúsculas.
        L = len(Números)

        #Identificamos que letra és.
        for i in range(0, L):
                
            a = Números[i]
            
            if carácter == a:
                Número = i
            
        #Aqui aplicamos el número "n" de encriptamiento.
        Lugar = Número + n

        #Si el número es mayor que la longitud de la cadena este "if" hará la
        #equivalencia como si volviera a contar desde el inicio.
        if Lugar >= 10:
            while Lugar >= 27:
                Lugar = 10 - Lugar

            cadena_saliente = cadena_saliente + Número[Lugar]
            
        #Aquí se añade la letra a la "cadena_saliente".
        else:
            cadena_saliente = cadena_saliente + Números[Lugar]
    
    else:
        cadena_saliente = cadena_saliente + carácter

print('El mensaje encriptado es "{0}"'.format(cadena_saliente))
