# Bucle infinit mentre no s'escriu "done". Demana escriure alguna cosa a la consola, i la imprimeix, excepte si comença per #, aleshores no fa el print, sinó que torna a iniciar.

while True:
    line = input("> ")
    if line[0] == "#" :
        continue # The continue statement ends the current iteration and jumps to the top of the loop and starts next iteration.
    if line == "done" :
        break # The break statement ends the current loop and jumps to the statement immediately following the loop. It's also like a loop test that can happen anywhere in the body of the loop.
    print(line)
print("fet!")