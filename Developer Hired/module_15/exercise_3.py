def verificar_sobrenome(nome):
    if 'SANTOS' in nome.upper():
        print(f'O nome {nome} possui a palavra SANTOS.')
    else:
        print(f'O nome {nome} NÃO possui a palavra SANTOS.')

nome = input('Digite o seu nome: ')

verificar_sobrenome(nome)