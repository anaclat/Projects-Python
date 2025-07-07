import random

def gerar_jogo():
    return sorted(random.sample(range(1, 61), 6))

def gerar_jogos(qtd):
    jogos = []
    for _ in range(qtd):
        jogos.append(gerar_jogo())
    return jogos

def main():
    while True:
        try:
            quantidade = int(input('Quantos jogos deseja gerar? '))
            if quantidade <= 0:
                print('Por favor, digite um número maior que zero.')
                continue
            break
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')
    
    jogos_gerados = gerar_jogos(quantidade)
    
    print('\nJogos gerados:')
    for i, jogo in enumerate(jogos_gerados, start=1):
        print(f"Jogo {i}: {jogo}")

main()