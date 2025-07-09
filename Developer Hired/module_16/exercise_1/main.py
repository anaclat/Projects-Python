from worker import Trabalhador
from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def cadastrar_trabalhador():
    trabalhador = Trabalhador()

    trabalhador.nome = input('Nome: ')

    while True:
        try:
            ano_nasc = int(input('Ano de nascimento: '))
            break
        except ValueError:
            print('Digite um ano válido.')

    trabalhador.idade = calcular_idade(ano_nasc)

    while True:
        try:
            trabalhador.clt = int(input('Carteira de trabalho (0 se não tem): '))
            break
        except ValueError:
            print('Digite um número válido.')

    if trabalhador.clt != 0:
        while True:
            try:
                trabalhador.ano_contratacao = int(input('Ano de contratação: '))
                trabalhador.salario = float(input('Salário: R$ '))
                break
            except ValueError:
                print('Entrada inválida. Tente novamente.')

        tempo_contribuicao = datetime.now().year - trabalhador.ano_contratacao
        trabalhador.aposentadoria = trabalhador.idade + (45 - tempo_contribuicao)

    return trabalhador

def mostrar_dados(trabalhador):
    print('\nCadastro realizado:')
    print(f'Nome: {trabalhador.nome}')
    print(f'Idade: {trabalhador.idade}')
    print(f'clt: {trabalhador.clt}')
    
    if trabalhador.clt != 0:
        print(f'Ano de contratação: {trabalhador.ano_contratacao}')
        print(f'Salário: R$ {trabalhador.salario:.2f}')
        print(f'Você poderá se aposentar com: {trabalhador.aposentadoria} anos')

def main():
    trabalhador = cadastrar_trabalhador()
    mostrar_dados(trabalhador)

main()