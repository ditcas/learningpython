# Exercici complet que donada una frase, compta quantes vegades hi ha cada paraula, i retorna la més repetida i les vegades que apareix.

import string

counts = dict()
line = input("Enter a line of text:")
# line = line.rstrip() Si la lectura fos d'un text, hauríem de suprimir els intros del final de cada línea.
line = line.translate(line.maketrans("","",string.punctuation)) #Elimina de la línea els signes de puntuació, perquè sinó, hola! i hola, serien dues paraules diferents.
line = line.lower() #Ho posa tot en minúscules, perquè sinó Hola i hola serien paraules diferents.
words = line.split()

for word in words :
    counts[word] = counts.get(word,0) + 1

# Busquem la paraula més repetida i quantes vegades ho està, és a dir, en el diccionari counts mirem qui té l'ítem valor més gran.

bigcount = None
bigword = None
for word,count in counts.items() :
    if bigcount is None or count > bigcount : # bigcount is None succeeix en la primera iteració, quan és la primera paraula que mirem, aquesta és per defecte la més repetida. Després ja comparem.
        bigcount = count
        bigword = word
print(bigword, bigcount)

# Manera alternativa. Ordenem el diccionari per l'ítem valor, i ens quedem amb el primer ítem. A més, si el següent ítem té el mateix valor (dos o més paraules igual de repetides), volem mostrar-los tots!

sort_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True) # count.items és una llista de tuples key-value. El resultat d'aquest sorted és una llista de tuples ordenades pel segon ítem, value, de gran a petit (reverse=true)

# sort_counts = sorted([ (value,key) for key,value in counts.items() ], reverse=True) Manera alternativa d'ordenar per valor. Creem una llista de tuples que inverteix les tuples de counts.items i posa primer el valor. Aleshores, sorted ordena aquesta llista pels valors, que és el que volíem. El que passa és que la llista final ordenada està invertida, primer té els valors i després la key.

# Si haguéssim volgut ordenar per key, aleshores és tant fàcil com
# sort_key_counts = sorted(counts.items())

maxims = list() # Creem una llista on col·locar les paraules més repetides

for tupla in sort_counts :
    if tupla[1] == sort_counts[0][1] : # Si el valor de la paraula de cada tupla és igual que el valor de la primera paraula del diccionari (que és la més gran perquè l'hem ordenat), l'afegim a la llista de maxims
        maxims.append(tupla)

print(maxims)