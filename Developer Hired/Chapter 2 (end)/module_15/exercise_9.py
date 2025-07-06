def adicionar_tupla(qtd=9):
    valores = tuple(
        int(input(f'Digite o {i+1}º valor: '))
        for i in range(qtd)
    )
    return valores

def relatorio_valores(valores):
    maior = max(valores)
    menor = min(valores)

    posicoes_maior = [i for i, v in enumerate(valores) if v == maior]
    posicoes_menor = [i for i, v in enumerate(valores) if v == menor]

    print('\nRELATÓRIO:')
    print(f'O MAIOR número é: {maior}, nas posições: {posicoes_maior}')
    print(f'O MENOR número é: {menor}, nas posições: {posicoes_menor}')

valores = adicionar_tupla()
relatorio_valores(valores)