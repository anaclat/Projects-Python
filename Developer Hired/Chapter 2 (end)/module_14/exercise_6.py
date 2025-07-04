def fatorial(numero,calculo=False):
    fatorial = 1

    print(f'O fatorial de {numero}! é:',end=' ')

    for indice in range(numero,0,-1):
        fatorial *= indice

        if calculo is True:
            caracter = 'x'
            if indice == 1:
                caracter  = '='
            print(f'{indice} {caracter}', end=' ')

    print(fatorial)

numero = int(input('Digite um número: '))

fatorial(numero,calculo=True)