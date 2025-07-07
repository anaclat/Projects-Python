termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 1

while contador < 9:
    print(f'O termo {contador} é {termo}.')
    termo += razao
    contador += 1
