from datetime import date
nascimento  = int(input('Digite o ano em que nasceu: '))
idade = date.today().year - nascimento

if 7 >= idade <= 9:
    print('Sua categoria é: FRALDINHA.')
elif 10 >= idade <=  11:
    print('Sua categoria é: DENTE DE LEITE.')
elif 12 >= idade <= 13:
    print('Sua categoria é: MIRIM.')
elif 14 >= idade <= 16:
    print('Sua categoria é: INFANTIL.')
elif 17 >= idade <=18:
    print('Sua categoria é: JUVENIL.')
elif 19 >= idade <=20:
    print('Sua categoria é: JUNIOR.')
else:
    print('Sua categoria é: PROFISSIONAL.')