# Escribe un programa que lee un archivo e imprime las letras en order decreciente de frecuencia. El programa debe convertir todas las entradas a minúsculas y contar solamente las letras a-z.
# El programa no debe contar espacios, dígitos, signos de puntuación, o cualquier cosa que no sean las letras a-z. Encuentra ejemplos de texto en idiomas  diferentes, y observa cómo la frecuencia de letras es diferente en cada idioma. Compara tus resultados con las tablas en https://es.wikipedia.org/wiki/Frecuencia_de_aparici%C3%B3n_de_letras.

import sys
import string

file = input("Indica el nom de l'arxiu: ")
if len(file) < 1 :  # Si faig intro quan em demana el nom de l'arxiu, com que té lingitud menor a 1, m'agafa per defecte text_catala.txt
    file = open("text_catala.txt")
else :
    try :
        file = open(file,"r")
    except :
        print("No s'ha pogut trobar l'arxiu:", file)
        sys.exit()

lletres = dict()

for line in file :
    line = line.rstrip()
    line = line.translate(line.maketrans("","",string.punctuation))
    line = line.translate(line.maketrans("","",string.digits))
    line = line.translate(line.maketrans("","",string.whitespace))
    line = line.lower()
    line = line.translate(line.maketrans("áàéèíïóòúü","aaeeiioouu"))
    for letter in line :
        lletres[letter] = lletres.get(letter,0) + 1

sort_lletres = sorted(lletres.items(), key=lambda x: x[1], reverse=True)

print(sort_lletres)