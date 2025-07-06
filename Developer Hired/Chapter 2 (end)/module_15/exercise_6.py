def adicionar_numeros():
    numeros = []
    numeros_par = []
    numeros_impar = []

    while True:
        try:
            numero = int(input('Digite um valor: '))
            numeros.append(numero)
        except ValueError:
            print('Valor inválido! Digite um número inteiro.')
            continue

        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        while continuar not in ('S', 'N'):
            continuar = input('Resposta inválida. Deseja continuar? [S/N] ').strip().upper()

        if numero % 2 == 0:
            numeros_par.append(numero)
        else:
            numeros_impar.append(numero)

        if continuar == 'N':
            break

    return numeros, numeros_par, numeros_impar

# Executando a função
numeros,  numeros_par, numeros_impar = adicionar_numeros()
print(f'\nA lista completa é: {numeros}.')
print(f'Os números pares são: {numeros_par}.')
print(f'Os números ípares são: {numeros_impar}.')