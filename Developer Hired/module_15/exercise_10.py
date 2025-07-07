def numeros_lista():
    numeros = []

    while True:
        try:
            numero = int(input('Digite um número: '))
            if numero not in numeros:
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
numeros.sort()
print(f'Os numeros não repetidos em ordem crescente são: {numeros}.')
