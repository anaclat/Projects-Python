def ler_dados_selecao():
    selecao = {}

    selecao['nome'] = input('Nome da seleção: ').strip()

    while True:
        try:
            partidas = int(input('Quantas partidas jogou na Copa de 2002? '))
            if partidas < 0:
                print('Número de partidas não pode ser negativo.')
                continue
            break
        except ValueError:
            print('Digite um número inteiro válido.')

    gols = []
    for i in range(1, partidas + 1):
        while True:
            try:
                gol = int(input(f'Gols feitos na partida {i}: '))
                if gol < 0:
                    print('Quantidade de gols não pode ser negativa.')
                    continue
                gols.append(gol)
                break
            except ValueError:
                print('Digite um número inteiro válido.')

    selecao['partidas'] = partidas
    selecao['gols'] = gols
    selecao['total'] = sum(gols)

    return selecao

def mostrar_dados(selecao):
    print(f'\nDesempenho da seleção {selecao["nome"]}:')
    for i, gols in enumerate(selecao['gols'], start=1):
        print(f'--> Na partida {i}, foram {gols} gols')
    print(f'\nFoi um total de {selecao["total"]} gols na Copa do Mundo de 2002')

def main():
    dados = ler_dados_selecao()
    mostrar_dados(dados)

main()