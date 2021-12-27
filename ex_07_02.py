# Escribe un programa que solicite un nombre de archivo y después lea ese archivo buscando las líneas que tengan la siguiente forma:X-DSPAM-Confidence: 0.8475 **Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla aparte para extraer el número decimal de la línea. Cuenta esas líneas y después calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al final del archivo, imprime el valor medio de “spam confidence”.

import sys

def identificador(str,marcador) : #donada una string i un marcador, extreu la subcadena (codi) posterior al marcador i la converteix en un float.
    posmarcador = str.find(marcador)
    if posmarcador == -1 :
            sys.exit("Error. No s'ha pogut trobar el marcador")
    try :        
        codi = float(str[posmarcador+20:posmarcador+26])
        return codi
    except :
        sys.exit("Error en transformar string to float")


file = input("Indica el nom de l'arxiu: ")
try :
    file = open(file,"r")
except :
    print("No s'ha pogut trobar l'arxiu:", file)
    sys.exit()

count = 0
sumatori = 0

# Si considerem que l'expressió "X-DSPAM-Confidence: codi" està pel mig de la línea. Aleshores en la funció "identificador" cal "codi = float(str[posmarcador+20:posmarcador+26])"

for line in file :
    if not "X-DSPAM-Confidence:" in line :
        continue
    count = count + 1
    sumatori = sumatori + identificador(line,"X-DSPAM-Confidence:")


# Si considerem que la frase comença i únicament conté "X-DSPAM-Confidence: codi". Aleshores en la funció "identificador" cal "codi = float(str[posmarcador+2:])" +2 perquè després del marcador ":" hi ha un espai

#for line in file :
#    if not line.startswith("X-DSPAM-Confidence:") :
#        continue
#    count = count + 1
#    sumatori = sumatori + identificador(line,":")

print("Promig Spam Confidence", sumatori/count)