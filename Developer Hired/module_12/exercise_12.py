nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))
media = (nota_1 + nota_2)/2

print(f'Sua média é: {media}.')

if media >= 7:
    print('Você está APROVADO.')
elif 5 >= media <= 6.9:
    print('Você está de RECUPERAÇÃO.')
else:
    print('Você está REPROVADO.')