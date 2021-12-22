# Write a program to prompt the user for hours and rate per hour to compute gross pay.

xh = input("How many hours have you done? ")
xe = input("What's your rate per hour? ")
gp = float(xh) * float(xe)
valor_arrodonit = round(gp, 3) # Arrodoneix el valor de gp, a 3 decimals
print("Gross pay:", valor_arrodonit)
