sacar = int(input('Qual valor você gostaria de sacar? '))

cinquenta = sacar//50
restou_50 = sacar - (50*cinquenta)

vinte = restou_50//20
restou_20 = restou_50 - (20*vinte)

cinco = restou_20//5
restou_5 = restou_20 - (5*cinco)

um = restou_5//1

print(f'Total de {cinquenta} cédula(s) de R$50.')
print(f'Total de {vinte} cédula(s) de R$20.')
print(f'Total de {cinco} cédula(s) de R$5.')
print(f'Total de {um} cédula(s) de R$1.')