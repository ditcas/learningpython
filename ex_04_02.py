# Reescribe el programa de calificaciones del capítulo anterior usando una función llamada calcula_calificacion, que reciba una puntuación como parámetro y devuelva una calificación como cadena.

import sys

def calcula_calificacion(puntuacio):
    if puntuacio > 1.0 or puntuacio < 0.0 :
        return "Error. La puntuació està fora del rang."
    elif puntuacio < 0.6 :
        return "Insuficient"
    elif puntuacio < 0.7 :
        return "Suficient"
    elif puntuacio < 0.8 :
        return "Bé"
    elif puntuacio < 0.9 :
        return "Notable"
    else :
        return "Excel·lent"


puntuacio = input("Introdueixi la puntuació entre 0.0 i 1.0: ")
try :
    puntuacio = float(puntuacio)
except :
    sys.exit("Puntuació incorrecta. Introdueixi un valor numèric.")

print(calcula_calificacion(puntuacio))