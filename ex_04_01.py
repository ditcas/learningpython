# Reescribe el programa de cálculo del salario, con tarifa-y- media para las horas extras, y crea una función llamada calculo_salario que reciba dos parámetros (horas y tarifa).

import sys #Llibreria que conté l'opció de fer sys.exit, que "surt" del programa.

def calcul_salari(hores, preu_hora) : # hores i preu hora són dos arguments/paràmetres de la funció que requereix que siguin passats a la funció per poder exectuar els càlculs. No són variables, no es guarden en cap memòria.

    jornada_base = 40

    if hores <= jornada_base :  # primer posar en l'if el cas més plausible, que és no fer hores extres.
        salari = hores * preu_hora
    else :
        hores_extres = hores - jornada_base
        salari_base = jornada_base * preu_hora
        salari_extra = hores_extres * 1.5 * preu_hora
        salari = salari_base + salari_extra

    return round(salari, 3) # Ends the function execution and "sends back" the result of the function


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


print("Salari:", calcul_salari(hores, preu_hora))