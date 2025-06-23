salario = float(input('Digite o salário do funcionário: '))

if salario > 1015.00:
    aumento = (salario*(13/100)) + salario
else:
    aumento = (salario*(27/100)) + salario

print(f'Quem ganhava R${salario} passa a ganhar R${aumento}.')