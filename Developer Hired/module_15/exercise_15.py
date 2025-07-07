from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def cadastrar_trabalhador():
    pessoa = {}
    pessoa['nome'] = input('Nome: ').strip()
    
    while True:
        try:
            ano_nasc = int(input('Ano de nascimento: '))
            break
        except ValueError:
            print('Digite um ano válido.')
    
    idade = calcular_idade(ano_nasc)
    pessoa['idade'] = idade

    while True:
        try:
            ctps = int(input('Carteira de trabalho (0 se não tem): '))
            break
        except ValueError:
            print('Digite um número válido.')
    
    pessoa['ctps'] = ctps

    if ctps != 0:
        while True:
            try:
                ano_contratacao = int(input('Ano de contratação: '))
                salario = float(input('Salário: R$ '))
                break
            except ValueError:
                print('Entrada inválida. Tente novamente.')
        
        pessoa['ano_contratacao'] = ano_contratacao
        pessoa['salario'] = salario
        tempo_contribuicao = datetime.now().year - ano_contratacao
        pessoa['Você poderá se aposentar com:'] = idade + (45 - tempo_contribuicao)
    
    return pessoa

def mostrar_dados(dados):
    print('\nCadastro realizado:')
    for chave, valor in dados.items():
        print(f'{chave.capitalize()}: {valor}')

def main():
    trabalhador = cadastrar_trabalhador()
    mostrar_dados(trabalhador)


main()