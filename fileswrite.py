file = open("sortida.txt","w") # "r" llegir, "r+"" llegir i sobreescriure (l'arxiu ha d'estar creat), "w" sobreescriure (si no està creat l'arxiu, el crea. Si està creat, esborra el contingut previ i escriu el nou), "a" afegir text al final

line1 = "Tu poesía surge por sí sola\n"
file.write(line1)
line2 = "en cuanto tú y el objeto se han vuelto uno."
file.write(line2)
file.close()

file = open("sortida.txt","a")
line3 = "\nY haciendo así debes soltar cualquier preocupación por ti mismo."
file.write(line3)
file.close()

file = open("sortida.txt","r")
text = file.read()
print(text)
file.close()