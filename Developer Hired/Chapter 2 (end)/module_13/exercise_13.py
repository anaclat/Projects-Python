from random import randint

numero = randint(0,10)
vitorias = 0

while True:
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar [P/I]: '))

    soma  = numero + jogador

    if soma % 2 == 0:
        if escolha ==  'P':
            vitorias += 1
            print(f'Você jogou {jogador} e o computador {numero}. Total de {soma}. DEU PAR, logo você GANHOU!')
        else:             
            print(f'Você jogou {jogador} e o computador {numero}. Total de {soma}. DEU PAR, logo você PERDEU!')
            break

    else:
        if escolha ==  'I':
            vitorias += 1
            print(f'Você jogou {jogador} e o computador {numero}. Total de {soma}. DEU ÍMPAR, logo você GANHOU!')
        else:             
            print(f'Você jogou {jogador} e o computador {numero}. Total de {soma}. DEU ÍMPAR, logo você PERDEU!')
            break

print(f'\nVocê venceu {vitorias} vez(es)!')