nome = input('Digite o seu nome: ')

def primeiro_ultimo(nome):
    print(f'Seu primeiro nome é: {nome.split(" ")[0]}')
    print(f'Seu último nome é: {nome.split(" ")[-1]}')

primeiro_ultimo(nome)