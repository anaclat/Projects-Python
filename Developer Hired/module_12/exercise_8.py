casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o se salário: '))
anos = int(input('Você pretende pagar em quantos anos? '))

prestacao = casa/(anos*12)
print(f'A prestação mensal será de R${prestacao}.')
pode_pagar = salario*(33/100)

if pode_pagar >= prestacao:
    print('Financiamento LIBERADO.')
else:
    print(f'O máximo que você pode pagar por mês é R${pode_pagar}. Financiamento NEGADO.')