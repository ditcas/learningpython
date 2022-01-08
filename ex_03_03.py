# Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:
import sys

puntuacio = input("Introdueixi la puntuació entre 0.0 i 1.0: ")
try :
    puntuacio = float(puntuacio)
except :
    sys.exit("Puntuació incorrecta. Introdueixi un valor numèric.")

# if i elif: Només executarà UNA de les opcions, i executarà la PRIMERA que trobi que sigui certa. Si després n'hi ha més que es compleixen, és igual, ja no hi entra. SI, SI NO, SI NO, SI NO...

if puntuacio > 1.0 or puntuacio < 0.0 :
    print("Error. La puntuació està fora del rang.")
elif puntuacio < 0.6 :
    print("Insuficient")
elif puntuacio < 0.7 :
    print("Suficient")
elif puntuacio < 0.8 :
    print("Bé")
elif puntuacio < 0.9 :
    print("Notable")
else :
    print("Excel·lent")