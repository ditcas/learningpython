# Exercici complet que donada una frase, compta quantes vegades hi ha cada paraula, i retorna la més repetida i les vegades que apareix.

import string

counts = dict()
line = input("Enter a line of text:")
# line = line.rstrip() Si la lectura fos d'un text, hauríem de suprimir els intros del final de cada línea.
line = line.translate(line.maketrans("","",string.punctuation)) #Elimina de la línea els signes de puntuació, perquè sinó, hola! i hola, serien dues paraules diferents.
# print(line)
line = line.lower() #Ho posa tot en minúscules, perquè sinó Hola i hola serien paraules diferents.
# print(line)
words = line.split()
# print(words)

for word in words :
    counts[word] = counts.get(word,0) + 1

# print(counts)

sorted()

bigcount = None
bigword = None
for word,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigcount = count
        bigword = word
print(bigword, bigcount)

