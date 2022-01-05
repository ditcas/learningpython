# Dictionaries are Python's most powerful data collection
# They have different names in different languages: Associative Arrays (Perl/PHP), Properties or Map or HashMap (Java), Property Bag (C#/ .Net)

# Dictionaries are like bags - no order
# LISTS index their entries based on the position in the list. 
# DICTIONARIES index using KEY/LABEL - VALUE

purse = dict() # empty dictionary
purse["money"] = 12
purse["candy"] = 3
print(purse)
print(purse["candy"])
purse["candy"] = purse["candy"] + 2
print(purse)

moneder = {"Judit" : 60, "Israel" : 50} # creating a dictionary
print(moneder)
# print(moneder["Dolors"]) Donaria Tracebak perquè Dolors no està en el diccionari
print("Dolors" in moneder) # Retorna False

# Dictionaries per COMPTAR elements

# Bucle sense method get menys eficient
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called GET() that does this.

# counts.get(name, 0)  equival a 
# if name in counts:
    # x = counts[name]
# else :
    # x = 0

# Bucle amb method get més eficient
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

# Extreure keys o values del dictionary
counts = {"chuck": 1, "fred": 42, "jan": 100}

print(list(counts.keys())) #És una llista amb les keys. 
print(list(counts.values())) #És una llista amb els values. Té el mateix ORDRE que la llista de keys.
print(list(counts.items())) #Són parells de dos valors, tuples

for key in counts :
    print(key, counts[key])
# bucle alternatiu
for key,value in counts.items() :
    print(key, value)







