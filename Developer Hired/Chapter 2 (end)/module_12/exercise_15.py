valor = float(input('Digite o valor do produto: '))

print(f'''FORMAS DE PAGAMENTO:
         [1] À VISTA - DINHEIRO
      [2] À VISTA - CARTÃO
      [3] PARCELADO (JUROS 15%)''')

escolha = int(input('Escolha sua opção: '))

if escolha == 1:
    pagar = valor - (valor*(10/100))
    print(f'Valor final do produto: R${pagar}.')

elif escolha == 2:
    pagar = valor - (valor*(5/100))
    print(f'Valor final do produto: R${pagar}.')

elif escolha == 3:
    pagar = valor + (valor*(15/100))
    print(f'Valor final do produto: R${pagar}.')

else:
    print('Digite uma opção válida.')