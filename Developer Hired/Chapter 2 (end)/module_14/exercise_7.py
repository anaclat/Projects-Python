def relatorio_notas(lista_notas,situacao=False):
    quantidade_notas = len(lista_notas)
    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)

    media = sum(lista_notas)/quantidade_notas

    relatorio = {
        'Quantidade': quantidade_notas,
        'Maior': maior_nota,
        'Menor': menor_nota,
        'Média': media
    }

    if situacao is True:
        if media >= 7:
            relatorio['Situacao'] = 'APROVADO'
        else:
            relatorio['Situacao'] = 'REPROVADO'

    return relatorio

lista_notas = (7,9,5)
relatorio  = relatorio_notas(lista_notas,situacao=True)
print(relatorio)