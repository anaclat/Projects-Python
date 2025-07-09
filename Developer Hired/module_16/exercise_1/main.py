from worker import Trabalhador
from datetime import datetime

def _validar_entrada_inteira(mensagem, erro_mensagem, min_val=None, max_val=None):
    #Função auxiliar para validar entrada de números inteiros.
    while True:
        try:
            valor = int(input(mensagem))
            if min_val is not None and valor < min_val:
                print(f"O valor deve ser maior ou igual a {min_val}.")
            elif max_val is not None and valor > max_val:
                print(f"O valor deve ser menor ou igual a {max_val}.")
            else:
                return valor
        except ValueError:
            print(erro_mensagem)

def _validar_entrada_float(mensagem, erro_mensagem, min_val=0.0):
    #Função auxiliar para validar entrada de números decimais (float).
    while True:
        try:
            valor = float(input(mensagem))
            if valor < min_val:
                print(f"O valor deve ser maior ou igual a {min_val}.")
            else:
                return valor
        except ValueError:
            print(erro_mensagem)

def cadastrar_trabalhador():
    #Coleta os dados do trabalhador e retorna um objeto Trabalhador.
    nome = input('Nome: ').strip()
    if not nome:
        print("O nome não pode ser vazio. Tente novamente.")
        return None # Retorna None para indicar que o cadastro falhou

    ano_nascimento = _validar_entrada_inteira(
        'Ano de nascimento: ',
        'Digite um ano válido.',
        min_val=1900, # Assume um ano de nascimento mínimo razoável
        max_val=datetime.now().year
    )

    clt = _validar_entrada_inteira(
        'Carteira de trabalho (0 se não tem): ',
        'Digite um número válido para a carteira de trabalho.'
    )

    ano_contratacao = None
    salario = None

    if clt != 0:
        ano_contratacao = _validar_entrada_inteira(
            'Ano de contratação: ',
            'Entrada inválida. Tente novamente.',
            min_val=ano_nascimento + 14, # Assume que a pessoa não pode ser contratada antes dos 14 anos
            max_val=datetime.now().year
        )
        salario = _validar_entrada_float(
            'Salário: R$ ',
            'Entrada inválida. Tente novamente.'
        )
    
    return Trabalhador(nome, ano_nascimento, clt, ano_contratacao, salario)

def mostrar_dados(trabalhador):
    #Exibe os dados do trabalhador.
    if trabalhador is None:
        print("\nNão foi possível exibir os dados, o cadastro falhou.")
        return

    print('\n--- Cadastro Realizado ---')
    print(f'Nome: {trabalhador.nome}')
    print(f'Idade: {trabalhador.idade} anos')
    print(f'CLT: {trabalhador.clt}')
    
    if trabalhador.clt != 0:
        print(f'Ano de contratação: {trabalhador.ano_contratacao}')
        print(f'Salário: R$ {trabalhador.salario:.2f}')
        if trabalhador.aposentadoria is not None:
            print(f'Você poderá se aposentar com: {trabalhador.aposentadoria} anos')
        else:
            print('Não foi possível calcular a idade de aposentadoria (dados incompletos).')
    else:
        print('Não possui carteira de trabalho registrada.')

def main():
    #Função principal do programa.
    trabalhador = cadastrar_trabalhador()
    mostrar_dados(trabalhador)

if __name__ == "__main__":
    main()