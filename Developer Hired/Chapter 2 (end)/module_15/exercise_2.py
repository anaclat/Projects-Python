def sao_ou_nao(cidade):
    if 'SÃO' == cidade.upper().split(' ')[0].strip():
        print(f'A cidade {cidade} possui a palavra SÃO.')
    else:
        print(f'A cidade {cidade} NÃO possui a palavra SÃO.')

cidade = input('Em qual cidade você nasceu? ')

sao_ou_nao(cidade)