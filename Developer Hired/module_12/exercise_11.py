from datetime import date

nascimento = int(input('Digite o ano em que nasceu: '))

ano_atual = date.today().year
idade = ano_atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')

if idade < 18:
    anos_falta = 18 - idade
    print(f'Ainda faltam {anos_falta} anos para se alistar.')
    ano_alistamento = ano_atual - anos_falta
    print(f'Seu alistamento será em {ano_alistamento}.')

elif idade > 18:
    anos_demora = idade - 18
    print(f'Você deveria ter se alistado há {anos_demora} anos atrás.')
    ano_alistamento = ano_atual - anos_demora
    print(f'Você deveria ter se alistado em {ano_alistamento}.')

else:
    print(f'Você tem que se alistar AGORA!')