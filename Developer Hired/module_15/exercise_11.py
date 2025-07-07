def numeros_lista():
    numeros = []

    while True:
        try:
            numero = int(input('Digite um número: '))
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        continuar = input('Gostaria de continuar? [S/N]: ').strip().upper()
        while continuar not in ('S', 'N'):
            continuar = input('Resposta inválida. Gostaria de continuar? [S/N]: ').strip().upper()

        if continuar == 'N':
            break

    return numeros

numeros = numeros_lista()

print(f'\nForam digitados: {len(numeros)} números.')
print(f'A lista ordenada de forma decrescente fica: {sorted(numeros, reverse=True)}')

if 7 in numeros:
    print('O número "7" está na lista!')
else:
    print('O número "7" não foi digitado.')
