# Bucle infinit mentre no s'escriu "done". Demana escriure alguna cosa a la consola, i la imprimeix, excepte si comença per #, aleshores no fa el print, sinó que torna a iniciar.

while True:
    line = input("> ")
    if line[0] == "#" :
        continue
    if line == "done" :
        break
    print(line)
print("fet!")