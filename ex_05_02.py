# Escribe otro programa que pida una lista de números como la anterior y al final muestre por pantalla el máximo y mínimo de los números, en vez de la media.


gran = None
petit = None

while True :

    numero = input("Introdueixi un número o teclegi la paraula fi per acabar: ")

    if numero == "fi" :
        break

    try : 
        numero = float(numero)
    except :
        print("Error, per favor introdueixi un valor numèric.")
        continue

    if gran is None and petit is None : # El primer valor que s'introdueix es guarda a gran i petit. Només s'executa la primera vegada.
        gran = petit = numero
    if numero > gran :
        gran = numero
    if numero < petit :
        petit = numero

if gran != None :
    print("El valor més gran introduit és el", gran, "i el més petit és el", petit)