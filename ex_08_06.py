# Bucle usant lists per fer el promig dels valors introduits. Si la quantitat de valors és elevada, no és tan eficient com ex_05_01 i ex_05_02, ja que aquí la list va necessitant memòria per emmagatzemar primer tots els valors i després fer l'operació, mentre que en 01 i 02 només es necessiten 2 variables que emmagatzemen un valor que es va sobreescrivint.

llistat = list()
while True :

    numero = input("Introdueixi un número o teclegi la paraula fi per acabar: ")

    if numero == "fi" :
        break

    try : 
        numero = float(numero)
    except :
        print("Error, per favor introdueixi un valor numèric.")
        continue

    llistat.append(numero)

sumatori = sum(llistat)
quantitat = len(llistat)
mitjana = sumatori/quantitat
maxim = max(llistat)
minim = min(llistat)

print("La suma dels valors introduits és", sumatori, "d'un total de", quantitat, "números. La mitjana aritmètica és", mitjana, ". El valor més gran és el", maxim, "i el valor més petit és el", minim)