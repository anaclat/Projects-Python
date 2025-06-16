primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for numero in range(1,9):
    print(f'O primeiro termo {numero} é {primeiro_termo}.')
    primeiro_termo += razao