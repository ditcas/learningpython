# Escribir un programa que clasifica cada mensaje de correodependiendo del día de la semana en que se recibió. Para hacer esto busca las líneas que comienzan con “From”, después busca por la tercer palabra y mantén un contador para cada uno de los días de la semana. Al final del programa imprime los contenidos de tu diccionario (el orden no importa).
# Escribe un programa para leer a través de un historial de correos, construye un histograma utilizando un diccionario para contar cuántos mensajes han llegado de cada dirección de correo electrónico, e imprime el diccionario.
# Agrega código al programa anterior para determinar quién tiene la mayoría de mensajes en el archivo.
# Este programa almacena el nombre del dominio (en vez de la dirección) desde donde fue enviado el mensaje en vez de quién envió el mensaje (es decir, la dirección de correo electrónica completa). Al final del programa, imprime el contenido de tu diccionario.

import sys

file = input("Indica el nom de l'arxiu: ")
try :
    file = open(file,"r")
except :
    print("No s'ha pogut trobar l'arxiu:", file)
    sys.exit()

day_counts = dict()
mail_counts = dict()
origin_counts = dict()

for line in file :
    if not line.startswith("From ") : #L'exercici demana incloure només els From_ i no els From:
        continue
    words = line.split()
    mail = words[1].split("@")
    day_counts[words[2]] = day_counts.get(words[2],0) + 1
    mail_counts[words[1]] = mail_counts.get(words[1],0) +1
    origin_counts[mail[1]] = origin_counts.get(mail[1],0) +1

print("Quantitat de mails rebuts per dia de la setmana", day_counts, "\n")
print("Quantitat de mails rebuts per persona", mail_counts, "\n")
print("Quantitat de mails rebuts per organització", origin_counts, "\n")

sort_mail_counts = sorted(mail_counts.items(), key=lambda x: x[1], reverse=True)

maxims = list() # Creem una llista on col·locar els mails més repetits

for tupla in sort_mail_counts :
    if tupla[1] == sort_mail_counts[0][1] : # Si el valor del mail de cada tupla és igual que el valor del primer mail (que és el més gran perquè l'hem ordenat), l'afegim a la llista de maxims
        maxims.append(tupla)

print("Persona o persones de les quals hem rebut més correus:", maxims)