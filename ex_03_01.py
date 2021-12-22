# Reescribe el programa del cálculo del salario para darle al empleado 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40

import sys #Llibreria que conté l'opció de fer sys.exit, que "surt" del programa.

hores = input("Introdueix les hores: ")
try : 
    hores = float(hores)
except :
    sys.exit("Error, per favor introdueixi un valor numèric.") # Comprovar que l'usuari ha introduit un valor numèric. No pots fiar-te mai de l'usuari. Al principi, posar sempre totes les comprovacions d'allò que pot portar a error.

preu_hora = input("Introdueix la tarifa per hora: ")
try: 
    preu_hora = float(preu_hora)
except :
    sys.exit("Error, per favor introdueixi un valor numèric.")

jornada_base = 40

if hores <= jornada_base :  # primer posar en l'if el cas més plausible, que és no fer hores extres.
    salari = hores * preu_hora
else :
    hores_extres = hores - jornada_base
    salari_base = jornada_base * preu_hora
    salari_extra = hores_extres * 1.5 * preu_hora
    salari = salari_base + salari_extra

salari_arrodonit = round(salari, 3)

print("Salari:", salari_arrodonit)