# Les Tuples són immutables, com les strings. No es poden canviar els elements. Això les diferencia de les Lists, que sí que són mutables.

valors = (5, 4, "zero") # Definida una 3-tupla
# valors[0] = 1  Resulta Tracebak perquè no es pot modificar en les tuples

# Assignació múltiple gràcies a les tuples
(x, y) = ("patata", 2)
print(x)
print(y)

# Es poden usar comparadors lògics en tuples. Compara els dos primers ítems, si són iguals, els segons... i així successivament. Si fessim un print de les tres següents seqüències, les tres són TRUE.
(1, 2) > (0, 3)
(1, 2) > (1, 1)
("Joan", "Alba") < ("Joan", "Alma")

# Veure dictionaries_exemple.py per com usar la funció SORTED per ordenar diccionaris, els quals cal expressar prèviament com a llistes amb dictionari.items(), una llista plena de 2-tuples (key-value). Aquestes tuples es poden voler ordenar per Key o per Value. Veure dictionaries_exemple.py línea 27 a 30.