def analisar_nome():
    nome = input('Digite o seu nome completo: ').strip()

    print(f'\nSeu nome em MAIÚSCULAS: {nome.upper()}')
    print(f'Seu nome em minúsculas: {nome.lower()}')

    total_letras = len(nome.replace(' ', ''))
    print(f'Seu nome tem {total_letras} letras.')

    primeiro_nome = nome.split()[0]
    print(f'Seu primeiro nome é "{primeiro_nome}" e tem {len(primeiro_nome)} letras.')

analisar_nome()