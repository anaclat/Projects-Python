peso  = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/(altura**2)

print(f'Seu IMC é: {imc}.')

if imc < 18.5:
    print('Você está abaixo do seu peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal. Parabéns!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida. ATENÇÃO!!!')