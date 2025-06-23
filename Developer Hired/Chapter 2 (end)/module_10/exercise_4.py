from random import randint

jogador_1  = randint(0,8)
jogador_2 = randint(0,8)
jogador_3 = randint(0,8)
jogador_4 = randint(0,8)

jogadores = [jogador_1,jogador_2,jogador_3,jogador_4]

dicionario =  {'jogadas': jogadores}

maior  = max(dicionario['jogadas'])
menor = min(dicionario['jogadas'])

print(f'De todas as jogadas {dicionario["jogadas"]}, o {maior} é a maior.')