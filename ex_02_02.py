# Write a program that uses input to prompt for their name and then welcomes them.
# Tres maneres diferents de printar el mateix usant les funcions de print: concatenar (+), end, sep

nom = input("El teu nom és: ")

print(f"Benvingut/da {nom}!") # La millor manera de fer-ho, usar cadenes f.

print("Benvingut/da", nom + "!")
print("Benvingut/da", nom, end = "!\n") # \n fa el salto de carro. Quan no posem el paràmetre end en un print el salto de carro el fa per defecte.
print("Benvingut/da ", nom, "!", sep = "")