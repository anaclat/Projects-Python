numero = int(input('Digite um número: '))

print('''
[1]- Converter para Binário
[2]- Converter para Octal
[3]- Converter para Hexadecimal
''')

opcao = int(input('Escolha sua opção de conversão: '))

if opcao == 1:
    binario = bin(numero)
    print(f'O número {numero} convertido para binário é: {binario}.')
elif opcao == 2:
    octal = oct(numero)
    print(f'O número {numero} convertido para octal é: {octal}.')
elif opcao == 3:
    hexadecimal = hex(numero)
    print(f'O número {numero} convertido para hexadecimal é: {hexadecimal}.')
else:
    print('Digite uma opção válida.')