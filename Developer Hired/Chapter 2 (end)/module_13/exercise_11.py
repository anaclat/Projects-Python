contador = 0
soma = 0
maior = 0
menor = 0

while True:
    numero = int(input('Digite um número: '))
    
    while True:
        continuar = input('Você quer continuar? [S/N] ').strip().upper()
        if continuar in ['S', 'N']:
            break
        else:
            print('Entrada inválida. Por favor, digite apenas S ou N.')

    contador += 1
    soma += numero

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    if continuar == 'N':
        break

media = soma / contador
print(f'\nMaior número digitado: {maior}. Menor número digitado: {menor}.')
print(f'\nA média dos números é {media:.2f}.')
