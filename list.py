# Definir llista i elements de la llista
list1 = ["red", 24, 98.6, [5, 6]]
print("El primer element de la llista és:", list1[0])

list1[0] = "blue"
print("La llista amb el primer element modificat:", list1)

# Funció per comptar quants elements té la llista
print("La llista té en total", len(list1), "elements")

# Bucle que recórre i compta els elements de la llista
count = 0
for item in list1 :
    print("L'ítem", item, "és el número", count, "de la llista")
    count = count + 1

# funció range que serveix com a variable d'iteració per recórrer els elements d'una llista. Per a veure la llista de números que genera, cal posar la funció list al davant.
print(list(range(5)))
print("Les posicions dels elements de la llista són", list(range(len(list1))))

# Bucle igual que l'anterior però més funcional gràcies a la variable d'iteració que genera "range"
for i in range(len(list1)) :
    print("L'ítem", list1[i], "és el número", i, "de la llista")

# Concatenar llistes
lista = [1, 4, 6]
listb = [3, 5, 8]
listab = lista + listb
print(listab)

# slicing a list. Funciona igual que en les strings.
print(lista[:2])

# List Methods: append, count, extend, index, insert, pop, remove, reverse, sort... veure documentació

lista.append(12) #Afegeix element 12 al final de la llista
print(lista)
print(12 in lista)
print(4 not in lista)

listab.sort() # ordena valors de petit a gran, o strings en ordre alfabètic. Si la llista conté valors i strings barrejat dona traceback.
print(listab)