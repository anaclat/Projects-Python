from random import randint

numero = randint(0,50)

chute = int(input("Digite um número: "))

tentativas = 0

while True:
    if numero == chute:
        print(f"Parabéns, você acertou! O número é {numero}. Você acertou em {tentativas} tentativa(s).")
        break

    else:
     print(f"Chute errado. Tente novamente.")
     if numero > chute:
        tentativas = tentativas + 1
        print("Digite um número maior.")
     elif numero < chute:
        tentativas = tentativas + 1
        print("Digite um número menor.")
     chute = int(input("Digite um número: "))