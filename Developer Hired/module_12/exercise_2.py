velocidade = int(input('Qual a velocidade do carro em km/h? '))
permitido = 110
multa = (velocidade -  permitido)*13

if velocidade > permitido:
    print(f'Você está a {velocidade}km/h, sendo que a velocidade permitida é de {permitido}km/h. Sua multa é de R$:{multa}.')
else:
    print('Siga a sua viagem!')