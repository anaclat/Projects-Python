contador = 0
soma = 0

while True:
    numero = int(input('Digite um número: [99 para parar] '))

    if numero == 99:
        break

    soma +=numero
    contador +=1

print(f'Você digitou {contador} números. A soma entre eles é: {soma}.')