def ler_dados():
    pessoas = []

    while True:
        nome = input('Digite o seu nome: ')

        genero = input('Digite o seu gênero: [M/F] ').upper()
        while genero not in ('M', 'F'):
            genero = input('Digite o seu gênero: [M/F] ').upper()

        idade = int(input('Digite a sua idade: '))

        continuar = input('Deseja cadastrar outra pessoa? [S/N]: ').upper()
        while continuar not in ('S', 'N'):
            continuar = input('Deseja cadastrar outra pessoa? [S/N]: ').upper()

        dados_pessoa = {'nome': nome, 'genero': genero, 'idade': idade}
        pessoas.append(dados_pessoa)

        if continuar == 'N':
            break

    return pessoas

def media_idade(pessoas):
    soma_idade = sum(p['idade'] for p in pessoas)
    media = soma_idade / len(pessoas)
    print(f'\nA média de idade é de {media:.1f} anos.')
    return media

def homens_cadastrados(pessoas):
    print('\nEsses são os homens cadastrados:')
    for pessoa in pessoas:
        if pessoa['genero'] == 'M':
            print(f'--> {pessoa["nome"]}')

def pessoas_acima_media(pessoas, media):
    print('\nPessoas acima da média de idade:')
    for pessoa in pessoas:
        if pessoa['idade'] > media:
            for chave, valor in pessoa.items():
                print(f'--> {chave.capitalize()}: {valor}')
            print('')

def main():
    pessoas = ler_dados()
    quantidade_pessoas = len(pessoas)
    print(f'\nForam cadastradas {quantidade_pessoas} pessoas.')

    media = media_idade(pessoas)
    homens_cadastrados(pessoas)
    pessoas_acima_media(pessoas, media)

main()