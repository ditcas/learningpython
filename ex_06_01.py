# Ejercicio 5: Toma el siguiente código en Python que almacena una cadena: str = 'X-DSPAM-Confidence:0.8475' Utiliza find y una parte de la cadena para extraer la porción de la cadena después del carácter dos puntos y después utiliza la función float para convertir la cadena extraída en un número de punto flotante.

import sys

def identificador(str,marcador) : #donada una string i un marcador, extreu la subcadena (codi) posterior al marcador i la converteix en un float.
    posmarcador = str.find(marcador)
    if posmarcador == -1 :
            sys.exit("Error. No s'ha pogut trobar el marcador")
    try :        
        codi = float(str[posmarcador+1:])
        return codi
    except :
        sys.exit("Error en transformar string to float")

str = "X-DSPAM-Confidence:0.8475"
marcador = ":"

print(identificador(str,marcador))