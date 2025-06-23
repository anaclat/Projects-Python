numero = (int(input('Digite um número: ')))

resto = numero%2

if resto == 0:
    print(f'O número que você escolheu ({numero}) é PAR.')
else:
    print(f'O númerp que você escolheu ({numero}) é ÍMPAR.')