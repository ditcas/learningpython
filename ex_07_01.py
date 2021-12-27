# Escribe un programa que lea un archivo e imprima su contenido todo en mayúsculas.

import sys

file = input("Indica el nom de l'arxiu: ")
try :
    file = open(file,"r")
except :
    print("No s'ha pogut trobar l'arxiu: ", file)
    sys.exit()

fhandle = file.read()
fhandleup = fhandle.upper()
print(fhandleup)