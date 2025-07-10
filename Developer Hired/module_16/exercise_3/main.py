from student import Aluno

def ler_alunos():
    alunos = []
    while True:
        nome = input('Nome do aluno (ou "sair" para encerrar): ').strip()
        if nome.lower() == 'sair':
            break

        aluno = Aluno(nome)

        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f'Nota {i} de {nome}: '))
                    aluno.adicionar_nota(nota)
                    break
                except ValueError:
                    print('Nota inválida. Digite um número entre 0 e 10.')

        aluno.calcular_media()
        alunos.append(aluno)
    return alunos

def mostrar_boletim(alunos):
    print('\nBoletim:')
    print(f'{"Nº":<4} {"Aluno":<20} {"Média":>6}')
    print('-' * 32)
    for i, aluno in enumerate(alunos):
        print(f'{i:<4} {aluno.nome:<20} {aluno.media:>6.2f}')

def consultar_notas(alunos):
    while True:
        print('\nDigite o número do aluno para ver suas notas (99 para sair):')
        try:
            opcao = int(input('Opção: '))
            if opcao == 99:
                print('Encerrando consulta.')
                break
            if 0 <= opcao < len(alunos):
                aluno = alunos[opcao]
                print(f'\nNotas de {aluno.nome}:')
                for i, nota in enumerate(aluno.notas, start=1):
                    print(f'  NOTA {i}: {nota}')
            else:
                print('Número inválido, tente novamente.')
        except ValueError:
            print('Entrada inválida, digite um número.')

def main():
    alunos = ler_alunos()
    if alunos:
        mostrar_boletim(alunos)
        consultar_notas(alunos)
    else:
        print('Nenhum aluno cadastrado.')

main()