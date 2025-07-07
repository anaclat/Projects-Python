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

def mostrar_resumo(selecoes):
    print('\nResumo das seleções cadastradas:')
    print(f'{"Código":<6} {"Seleção":<20} {"Total de Gols":>15}')
    print('-' * 45)
    for i, selecao in enumerate(selecoes):
        print(f'{i:<6} {selecao["nome"]:<20} {selecao["total"]:>15}')

def consultar_selecao(selecoes):
    while True:
        try:
            codigo = int(input('\nDigite o código da seleção para ver detalhes (99 para sair): '))
            if codigo == 99:
                print('Encerrando consulta.')
                break
            if 0 <= codigo < len(selecoes):
                selecao = selecoes[codigo]
                print(f'\nDesempenho da seleção {selecao["nome"]}:')
                for i, gols in enumerate(selecao['gols'], start=1):
                    print(f'--> Na partida {i}, foram {gols} gols')
                print(f'\nFoi um total de {selecao["total"]} gols na Copa do Mundo de 2002')
            else:
                print('Código inválido.')
        except ValueError:
            print('Digite um número válido.')

def main():
    selecoes = []

    while True:
        print('\nCadastro de Seleção')
        selecao = ler_dados_selecao()
        selecoes.append(selecao)

        continuar = input('Deseja adicionar outra seleção? [S/N]: ').strip().lower()
        if continuar != 's':
            break

    if selecoes:
        mostrar_resumo(selecoes)
        consultar_selecao(selecoes)
    else:
        print('Nenhuma seleção foi cadastrada.')

main()