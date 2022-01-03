# Escribir un programa para abrir el archivo romeo.txt y leerlo línea por línea. Para cada línea, dividir la línea en una lista de palabras utilizando la función split. Para cada palabra, revisar si la palabra ya se encuentra previamente en la lista. Si la palabra no está en la lista, agregarla a la lista. Cuando el programa termine, ordenar e imprimir las palabras resultantes en orden alfabético.

file = open("romeo.txt","r")

lista = list()

for line in file :
    words_for_line = line.split()

    for word in words_for_line :

        if word not in lista :
            lista.append(word)

        # Manera alternativa de fer-ho sense usar l'operador "in, not in". Cal usar bucles anidats, i cal també fer cas concret de si la llista està buida. Cal usar també un chivato de False/True, en aquest cas word_exists.
        # if len(lista) == 0 : 
        #     lista.append(word)

        # word_exists = False
        # for existing_word in lista :

        #     if word == existing_word :
        #         word_exists = True
        
        # if word_exists == False :
        #     lista.append(word)

lista.sort()
print(lista)