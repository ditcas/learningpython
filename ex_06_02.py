# Lee la documentación de los métodos de cadenas en https://docs.python.org/library/stdtypes.html#string-methods Quizá quieras experimentar con algunos de ellos para asegurarte de entender como funcionan.

str = "www.example.com"

print(str[0]) # imprimeix el que hi ha guardat en l'índex 0 de la cadena.

print(len(str)) # longitud de la cadena.

strip = str.strip("om") # elimina l'expressió "om" si la troba al principi o al final de la cadena. Si no li posem argument elimina els espais en blanc del davant i darrere de la cadena. Veure també lstrip i rstrip.

print(strip)
print(len(strip))

# Recórrer una cadena

word = "banana"
count = 0

for letter in word : # Definite loop. Sap com començar, b, avança sol, i sap quan acabar. "Per cada un dels ítems de la cadena..."
    if letter == "a" :
        count = count + 1

print(count)

# Slicing strings

s = "Monty Python"
print(s[0:4]) # Des de l'ítem 0 fins al 4 no inclòs
print(s[6:7])
print(s[6:20]) # Si et passes de llarg amb un índex, no passares, para quan la cadena s'acaba.
print(s[:2]) # Si no hi ha número primer, s'entèn que és des de l'inici de la cadena.
print(s[8:]) # Del 8 fins al final
print(s[:]) # tot. No té molt sentit, posaríem print(s).

# IN as a logical operator

fruit = "banana"

"n" in fruit # TRUE
"m" in fruit # FALSE

# string comparison

# < > compara per ordre alfabètic, i considera les majúscules més grans que les minúscules.

# String library

# METHODS: Functions that are already built into every string. We invoke them by appending the function to the string. These functions do not modify the original string.

print("Hi There".lower()) # Nova string tota en minúscules. 
# Quan un usuari ens proporciona informació a través d'un input, és útil passar-ho a minúscules perquè no et pots fiar de l'usuari, i després quan s'hagi de mostrar ja ho capitalitzem nosaltres.

# Algunes de les més comuns són: capitalize, center, endswith, find, lstrip, rstrip, strip, replace, lower, upper, startswith...

# lstrip, rstrip, strip, s'usen majoritàriament per eliminar espais en blanc de l'esquerra, dreta o ambdós costats de la variable que pot haver introduit l'usuari en escriure.
