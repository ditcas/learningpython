# Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla el sumatori, la cantidad de números y la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, detecta su fallo usando try y except, muestra un mensaje de error y pasa al número siguiente.

def mitjana(sumatori, quantitat) :
    if quantitat == 0 :
        return 0

    return round(sumatori / quantitat, 3)

sumatori = 0
quantitat = 0

while True :

    numero = input("Introdueixi un número o teclegi la paraula fi per acabar: ")

    if numero == "fi" :
        break

    try : 
        numero = float(numero)
    except :
        print("Error, per favor introdueixi un valor numèric.")
        continue

    quantitat = quantitat + 1
    sumatori = sumatori + numero


print("La suma dels valors introduits és", sumatori, "d'un total de", quantitat, "números. La mitjana aritmètica és", mitjana(sumatori, quantitat))