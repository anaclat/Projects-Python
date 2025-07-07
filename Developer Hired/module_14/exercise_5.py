from datetime import date

def verificar_idade(nascimento):
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    print(f'Você tem: {idade} anos.')

    if 18 <= idade <= 60:
        return 'VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade > 60:
        return 'VOTO OPCIONAL.'
    else:
        return 'VOTO NEGADO.'
    
nascimento = int(input('Em que ano você nacseu? '))
voto = verificar_idade(nascimento)
print(voto)