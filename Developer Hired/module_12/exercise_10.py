primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))

if primeiro > segundo:
    print(f'O {primeiro} é maior que o {segundo}.')

elif primeiro < segundo:
    print(f'O {segundo} é maior que o {primeiro}.')
else:
    print('Ambos são iguais.')