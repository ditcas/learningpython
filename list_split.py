# Prova de realitzar el mateix exercici de ex_07_02 amb la comanda "split".

# Escribe un programa que solicite un nombre de archivo y después lea ese archivo buscando las líneas que tengan la siguiente forma:X-DSPAM-Confidence: 0.8475 **Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla aparte para extraer el número decimal de la línea. Cuenta esas líneas y después calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al final del archivo, imprime el valor medio de “spam confidence”.

import sys

file = input("Indica el nom de l'arxiu: ")
try :
    file = open(file,"r")
except :
    print("No s'ha pogut trobar l'arxiu:", file)
    sys.exit()

count = 0
sumatori = 0

# La línea és "X-DSPAM-Confidence: 0.7002", si fem "split" per defecte separa per l'espai, i per tant transforma una string en una llista, que té en aquest cas dos elements, X-DSPAM-Confidence: i 0.7002.

for line in file :
    if not "X-DSPAM-Confidence:" in line :
        continue
    count = count + 1
    words = line.split()
    try :        
        codi = float(words[1])
    except :
        sys.exit("Error en transformar string to float")
    sumatori = sumatori + codi


print("Promig Spam Confidence", sumatori/count)