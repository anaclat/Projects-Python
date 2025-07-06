def ler_numero_inteiro(mensagem):
    numero = input(mensagem)

    while numero.isnumeric() is False:
        print(f'ERROU! Digite novamente.')
        numero = input(mensagem)

    return numero

numero_inteiro = ler_numero_inteiro('Digite um número: ')
print(f'Você acabou de digitar: {numero_inteiro}.')