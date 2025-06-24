from datetime import date

nascimento = int(input('Digite o ano em que nasceu: '))

ano_atual = date.today().year
idade = ano_atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')