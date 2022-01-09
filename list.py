list1 = ["red", 24, 98.6, [5, 6]] # A list element can be any Python object, even another list.

print(list1[0]) # Imprimeix el primer element de la llista
print(list1[1]) # Imprimeix el segon element de la llista
print(list1[-1]) # Imprimeix l'últim element de la llista
print(f"El penúltim element de la llista és el {list1[-2]}.") # També es poden usar cadenes f en llistes

list1[0] = "blue" #modifico el primer element de la llista
print("La llista amb el primer element modificat:", list1)

# Funció per comptar quants elements té la llista
print("La llista té en total", len(list1), "elements")

# Bucle que recórre i compta els elements de la llista
count = 0
for item in list1 :
    print("L'ítem", item, "és el número", count, "de la llista")
    count = count + 1

# funció range que serveix com a variable d'iteració per recórrer els elements d'una llista. Per a veure la llista de números que genera, cal posar la funció list al davant.
print(list(range(5))) # Genera una llista de valors del 0 al 5 no inclòs
print(list(range(2,11,3))) # Genera una llista que comença en el 2 i avança de 3 en 3 fins arribar a 10.
print("Les posicions dels elements de la llista són", list(range(len(list1))))

# Bucle igual que l'anterior però més funcional gràcies a la variable d'iteració que genera "range"
for i in range(len(list1)) :
    print("L'ítem", list1[i], "és el número", i, "de la llista")

# Bucle que genera els quadrats dels primers 10 nombres
squares = list()

for nombre in range(1,11) :
    squares.append(nombre**2)

print("Llista dels quadrats dels primers 10 nombres", squares)

# LLISTES PER COMPRENSIÓ
# La mateixa llista creada abans però amb un codi més eficient, anomenat llista per comprensió
squares2 = [nombre**2 for nombre in range(1,11)]
print("Llista per comprensió dels quadrats dels primers 10 nombres", squares2)

# Concatenar llistes
lista = [1, 4, 6]
listb = [3, 5, 8]
listab = lista + listb
print("Llist a i llista b concatenades", listab)

# slicing a list. Funciona igual que en les strings.
print("Llista a del principi a l'element índex 2 no inclòs", lista[:2])

# List Methods: append, count, extend, index, insert, pop, remove, reverse, sort... veure documentació

lista.append(12) #Afegeix element 12 al final de la llista
print("Llista a amb element 12 afegit al final", lista)
print(12 in lista) # Saber si un element està o no la llista. Retorna True o False
print(4 not in lista)

# Afegir elements en qualsevol posició
lista.insert(1, 5)
print("Llista a amb l'element 5 afegit en la posició índex 1", lista)

# Eliminar un element si en sabem la posició. Després no es pot accedir a l'element eliminat.
del lista[3]
print("Llista a sense el quart element", lista)

# Eliminar element de la llista i guardar-lo en una variable per poder-lo usar després
print("La llista a en aquests moments és aquesta:", lista)
pop_element = lista.pop(1) #Elimino el segon element i el guardo en la variable pop_element. Si no posem argument, elimina l'últim element per defecte.
print("Després d'eliminar el segon element la llista a és aquesta:", lista)
print(f"L'element eliminat és el {pop_element}")

# Eliminar el primer element de la llista que coincideixi amb el valor donat. Si l'element estigués repetit, i volguessim eliminar-los tots, caldria fer bucle.
fruites = ["aguacate", "meló", "síndria", "taronja", "plàtan"]
citric = "taronja"
fruites.remove(citric)
print(f"Després d'eliminar la fruita cítrica {citric}, la llista queda:", fruites)


# Ordenar valors de petit a gran, o strings en ordre alfabètic (Ojo: sempre considera les majúscules més grans que les minúsucles). Si la llista conté valors i strings barrejat dona traceback.
# El mètode SORT modifica la llista de manera permanent
print("La llista ab abans d'ordenar:", listab)
listab.sort() 
print("Llista ab ordenada", listab)

# Si no volem modificar la llista original, només mostrar per un moment la llista ordenada, usem SORTED
print(fruites)
print(sorted(fruites, reverse=True)) #usem reverse per si volem ordre descendent
print(fruites)

# Invertir la llista (que no vol dir ordenar)
fruites.reverse()
print(fruites)

# Fer una còpia d'una llista
fruites_prefe = fruites[:] #Cal posar el [:]
fruites_prefe.append("maduixa")
print("fruites preferides:", fruites_prefe)
print("fruites", fruites) # Són dues llistes independents. Podem fer canvis a cada una per separat.
# En canvi si fem
fruites_prefe2 = fruites # fruites_prefe2 no és una llista independent, simplement li estem dient que aquesta variable apunti també a la mateixa llista de fruites. Si fem un canvi a fruites_prefe2 o a fruites, canviaran les dues llistes, perquè de fet, són la mateixa, apunten al mateix objecte.
fruites_prefe2.append("nabiu")
print("fruites", fruites)
print("fruites preferides 2", fruites_prefe2)
