from math import hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa tem um comprimento de {hipotenusa}.')