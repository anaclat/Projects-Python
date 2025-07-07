def cadastrar_dados():
    nomes = []
    pesos = []

    while True:
        nome = input('Digite seu nome: ')
        try:
            peso = float(input('Digite seu peso (kg): '))
        except ValueError:
            print("Por favor, digite um número válido para o peso.")
            continue

        nomes.append(nome)
        pesos.append(peso)

        while True:
            continuar = input('Gostaria de continuar? [S/N]: ').strip().upper()
            if continuar in ('S', 'N'):
                break
            else:
                print('Resposta inválida. Digite "S" para continuar ou "N" para sair.')

        if continuar == 'N':
            break

    return nomes, pesos

nomes, pesos = cadastrar_dados()

maior_peso = max(pesos)
menor_peso = min(pesos)

mais_pesados = [nomes[i] for i in range(len(pesos)) if pesos[i] == maior_peso]
mais_leves = [nomes[i] for i in range(len(pesos)) if pesos[i] == menor_peso]

# Resultado
print(f'Total de pessoas cadastradas: {len(nomes)}')
print(f'O maior peso foi {maior_peso}kg. Pessoa(s) com esse peso: {", ".join(mais_pesados)}.')
print(f'O menor peso foi {menor_peso}kg. Pessoa(s) com esse peso: {", ".join(mais_leves)}.')
