def adicionar_tupla():
    return (
        int(input('Digite o primeiro valor: ')),
        int(input('Digite o segundo valor: ')),
        int(input('Digite o terceiro valor: ')),
        int(input('Digite o quarto valor: '))
    )

def relatorio_valores(valores):
    print(f'O número "7" aparece {valores.count(7)} vez(es).')
    print(f'O número "6" foi digitado na posição: {valores.index(6)}.')

    print(f'Os números pares são: ', end='')
    for valor in valores:
        if valor % 2 == 0:
            print(valor, end='  ')
    print()

valores = adicionar_tupla()
relatorio_valores(valores)