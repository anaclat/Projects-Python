numero = int(input('Digite um número: '))

contador = numero
fatorial = 1

while contador > 0:
    fatorial*=contador
    contador -=1

print(f'O fatorial de {numero} é {fatorial}.')