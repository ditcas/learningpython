# Algunas veces cuando los programadores se aburren o quieren divertirse un poco, agregan un inofensivo Huevo de Pascua a su programa. Modifica el programa que pregunta al usuario por el nombre de archivo para que imprima un mensaje divertido cuando el usuario escriba “na na boo boo” como nombre de archivo.

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
    if file == "na na boo boo" :
        print("NA NA BOO BOO TU! T'HE PILLAT!")
    else :
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