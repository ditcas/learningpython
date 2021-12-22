# Write a program that uses input to prompt for their name and then welcomes them.
# Tres maneres diferents de printar el mateix usant les funcions de print: concatenar (+), end, sep

nom = input("El teu nom és: ")
print("Benvingut/da", nom + "!")
print("Benvingut/da", nom, end = "!\n") # \n fa el salto de carro
print("Benvingut/da ", nom, "!", sep = "")