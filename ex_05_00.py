llista = [9, 41, 12, 3, 74, 15]
petit = llista[0]

for numero in llista : #Per cada un dels elements de la llista
    if numero < petit :
        petit = numero
#    print(petit, numero)

print("El valor més petit és el", petit)