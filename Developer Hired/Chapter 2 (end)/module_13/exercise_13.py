from random import randint

numero = randint(0,10)

while True:
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar [P/I]: '))

    soma  = numero + jogador

    if soma % 2 == 0:
        if escolha ==  'P':
            print()