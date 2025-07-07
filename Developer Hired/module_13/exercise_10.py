from time import sleep

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))


while True:
    print('''
    Escolha uma opção:
        [1] somar
        [2] multiplicar
        [3] maior e menor
        [4] trocar números
        [5] sair do programa
''')    

    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        soma = primeiro_numero + segundo_numero
        print(f'O resultado de {primeiro_numero} + {segundo_numero} é: {soma}.')
    
    elif opcao == 2:
        multiplicacao = primeiro_numero*segundo_numero
        print(f'O resultado de {primeiro_numero} X {segundo_numero} é: {multiplicacao}.')

    elif opcao == 3:
        if segundo_numero >  primeiro_numero:
            print(f'{segundo_numero} é maior que {primeiro_numero}.')
        elif segundo_numero < primeiro_numero:
             print(f'{primeiro_numero} é maior que {segundo_numero}.')
        else:
            print(f'Os números são iguais.')
    elif opcao == 4:
        print('Informe novos números...')
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))

    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('Fim do programa.')
        break

    else:
        print('Digite uma opção válida!')
