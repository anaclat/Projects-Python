from random import randint

numero = randint(0,5)

resposta  = int(input('Tente adivinhar o número que eu pensei: '))

if resposta == numero:
    print('Parabéns! Você venceu!')
else:
    print(f'Você perdeu! Eu pensei no número {numero}.')