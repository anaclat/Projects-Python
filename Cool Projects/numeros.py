from random import randint

numero = randint(0,100)

chute = int(input("Digite um número: "))

while True:
    if numero == chute:
        print(f"Parabéns, você acertou! O número é {numero}.")
        break

    else:
     print(f"Chute errado. Tente novamente.")
     if numero > chute:
        print("Digite um número maior.")
     elif numero < chute:
        print("Digite um número menor.")
     chute = int(input("Digite um número: "))
