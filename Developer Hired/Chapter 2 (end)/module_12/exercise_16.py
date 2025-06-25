from random import randint

jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)

print('''
Vamos jogar:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA
   ''')

usuario = int(input('Faça sua jogada: '))

print(f'O computador jogou {jogadas[computador]} e você jogous {jogadas[usuario]}.')

if computador == 0:
    print(f'')