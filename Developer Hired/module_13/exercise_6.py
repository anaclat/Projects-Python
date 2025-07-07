termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 1

while contador < 9:
    print(f'O termo {contador} é {termo}.')
    termo += razao
    contador += 1


while True:
    mais_termo = int(input('Deseja ver mais quantos termos? [0 para sair]. '))

    contador_novo = contador + mais_termo
    while contador < contador_novo:
        print(f'O termo {contador} é {termo}.')
        termo += razao
        contador += 1


    if mais_termo == 0:
        break