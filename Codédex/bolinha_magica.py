from random import randint

pergunta = str(input('Faça uma pergunta: '))

numero = randint(0,8)

if numero == 1:
  print('Com certeza.')
elif numero == 2:
  print('Sem dúvida.')
elif numero == 3:
  print('Pergunta burra, tente novamente.')
elif numero == 4:
  print('Pergunte novamente mais tarde.')
elif numero == 5:
  print('Melhor não contar agora.')
elif numero == 6:
  print('Minhas fontes dizem que não.')
elif numero == 7:
  print('Perspectiva não tão boa.')
else:
  print('Muito duvidoso.')