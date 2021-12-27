file = open("mail.txt","r")

#Recórrer cada línea i la va imprimint. For __ in ___ detecta què és, si és un arxiu llegeix línea a línea, si és un array/llista, llegeix element a element, si és una string caràcter a caràcter.
for line in file :
    line = line.rstrip() #Com que la funció print fa per defecte un "intro" al final, i el file també té un intro al final de cada frase, elimino l'intro del file perquè sinó surt doble intro.
#    print(line)

file.seek(0) # L'apuntador del text es troba al final de l'arxiu després de recórre'l. Cal tornar-lo a posar a l'inici.

#Recórrer cada línea i les va contant.
count = 0
for line in file :
    count = count + 1
#print("L'arxiu té", count, "línies")

file.seek(0) # L'apuntador del text es troba al final de l'arxiu després de recórre'l. Cal tornar-lo a posar a l'inici.

#Guarda tot el text a la variable, com una string. L'intro compta com un caràcter.
inp = file.read()
#print("L'arxiu té", len(inp), "caràcters")
#print(inp)

file.seek(0)

#Searching through a file
for line in file :
    if line.startswith("From") :
        line = line.rstrip()
#        print(line)

file.seek(0)

# Manera alternativa de fer exercici anterior, on el codi del que volem fer queda al final i per tant estèticament pot ser millor

for line in file :
    if not line.startswith("From") :
        continue
    line = line.rstrip()
#    print(line)

file.seek(0)


# Buscar i seleccionar línies que continguin amb "in"
for line in file :
    if not "trapella" in line :
        continue
    line = line.rstrip()
#    print(line)

# Cuando estás leyendo y escribiendo archivos, puedes tener problemas con los espacios en blanco. Esos errores pueden ser difíciles de depurar debido a que los espacios, tabuladores, y saltos de línea son invisibles normalmente. La función nativa repr puede ayudarte. Recibe cualquier objeto como argumento y devuelve una representación del objeto como una cadena. En el caso de las cadenas, representa los espacios en blanco con secuencias de barras invertidas. Otro problema que podrías tener es que diferentes sistemas usan diferentes caracteres para indicar el final de una línea. \n, \r ... Para la mayoría de los sistemas, hay aplicaciones que convierten de un formato a otro.