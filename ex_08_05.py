import sys


file = input("Indica el nom de l'arxiu: ")
try :
    file = open(file,"r")
except :
    print("No s'ha pogut trobar l'arxiu:", file)
    sys.exit()

count = 0

for line in file :
    if not line.startswith("From ") : #L'exercici demana incloure només els From_ i no els From:
        continue
    count = count + 1
    words = line.split()
    print(words[1])

print("Hi ha", count, "línies a l'arxiu que comencin per la paraula From")