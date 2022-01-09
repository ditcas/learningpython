# Un = no significa igualtat d'expressions com en matemàtiques, sinó que significa ASSIGNACIÓ, és a dir, que primer executa l'expressió de la dreta i després la guarda a la variable de l'esquerra. El valor guardat pot ser actualitzat reemplaçant el valor antic per un de nou.
x = 5
x = x+1
print(x)

# Quan una variable volem indicar que el seu valor es consideri com una constant i per tant no s'alteri al llarg del programa, ho marcarem estèticament posant el nom de la variable tot en majúscules. Python no té tipologies de constants integrades, tot són variables.
CONSTANT_MAX = 5000

# Type
cadena = "Hello world"
print(type(cadena))
x = 1
print(type(x))
x = 98.6
print(type(x))

# N'hi ha d'altres, combinació d'aquests.
# Si en una expressió hi ha un int i un float barrejats, la resposta sempre estarà en format float.
# Podem escriure valors grans separant les xifres amb guió baix per veure-ho millor, no afecta a Python:
# 10000000000 és el mateix que 10_000_000_000
# # També es pot convertir usant les funcions int() i float()

print(float(42))

# També es pot convertir una string amb números en un int o float
cadena = "123" # OJO Si hi ha lletres dóna error.
print("Type inicial: ", type(cadena))
cadena = float(cadena)
print("Type després de float(): ", type(cadena))
print(cadena)

# Numeric expressions - Veure ex_02_04
# + (sumar per int i float, concatenar per strings(enganxat, sense espais))
# -, *, / (restar, multiplicar, dividir) La divisió sempre retorna un float.
# ** (potència)
# % (residu d'una divisió)
# Jerarquia: D'esquerra a dreta. Parèntesis, potència, * i /, + i -.


# INPUT - Veure ex_02_02
# input() We can instruct Python to pause and read data from the user. Returns always a string.

name = input("Who are you? ")
print("Welcome", name)

# CADENAS F (formato) : Una manera d'escriure variables dins d'una única cadena
print(f"Welcome {name}")

# Comparison operators

# < less than
# <= less than or equal to
# == equal to
# >= greater than or equal to
# > greater than
# != not equal
# They look at the variables but do not change the variables

# CONDITIONAL - EX_03
# COMPROVACIONS: TRY - EXCEPT - EX_03
# FUNCTIONS - EX_04
# BUCLES - loops_continue_break.py i EX_05
# STRINGS - EX_06
# ARCHIVOS - filesread.py i fileswrite.py i EX_07

# DATA STRUCTURES

# Algorithms: A set of rules or steps used to solve a problem.
# Data structures: A particular way of organizing data in a computer.
# Collection: many values in a single "variable": List, Dictionary, Tuple.

# Una list és mutable, una string i una tuple són immutables. Les keys d'un dictionary són immutables, els values són mutables.

# LIST - list_split.py, list.py, EX_08

# DICTIONARIES - dictionaries_exemple.py, dictionaries.py i EX_09
# TUPLES  - tuples.py i EX_10
