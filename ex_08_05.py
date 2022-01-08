# Escribir un programa para leer a través de datos de una bandeja de entrada de correo y cuando encuentres una línea que comience con “From”, dividir la línea en palabras utilizando la función split. Estamos interesados en quién envió el mensaje, lo cual es la segunda palabra en las líneas que comienzan con From. Tendrás que analizar la línea From e imprimir la segunda palabra de cada línea From, después tendrás que contar el número de líneas From(no incluir From:) e imprimir el total al final.

import sys


file = input("Indica el nom de l'arxiu: ")
try :
    file = open(file,"r")
except :
    print("No s'ha pogut trobar l'arxiu:", file)
    sys.exit()

count = 0

for line in file :
    if not line.startswith("From ") : #L'exercici demana incloure només els From_ i no els From:
        continue
    count = count + 1
    words = line.split()
    print(words[1])

print("Hi ha", count, "línies a l'arxiu que comencin per la paraula From")