from random import randint

numero = randint(0,8)
contador_p = 0

while True:
    contador_p +=1
    palpite = int(input('Digite seu palpite: '))
    
    if numero == palpite:
        print(f'Parabéns, o numero é {numero}. Você acertou com {contador_p} tentativas! ')
        break

    else:
        if numero < palpite:
            print(f'Menos que {palpite}... Tente novamente! ')
        else:
            if numero > palpite:
                print(f'Maior que {palpite}... Tente novamente! ')