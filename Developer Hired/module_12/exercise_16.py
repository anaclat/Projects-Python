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

print(f'O computador jogou {jogadas[computador]} e você jogou {jogadas[usuario]}.')

if computador == 0:
   if usuario == 0:
        print(f'DEU EMPATE.')
   elif usuario == 1:
        print('VOCÊ VENCEU.')
   elif usuario == 2:
       print('O COMPUTADOR VENCEU')

if computador == 1:
   if usuario == 1:
        print(f'DEU EMPATE.')
   elif usuario == 2:
        print('VOCÊ VENCEU.')
   elif usuario == 0:
       print('O COMPUTADOR VENCEU')

if computador == 2:
   if usuario == 2:
        print(f'DEU EMPATE.')
   elif usuario == 0:
        print('VOCÊ VENCEU.')
   elif usuario == 1:
       print('O COMPUTADOR VENCEU')

else:
    print('OPÇÃO INVÁLIDA!')