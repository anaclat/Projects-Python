def ler_alunos():
    alunos = []
    while True:
        nome = input('Nome do aluno (ou "sair" para encerrar): ').strip()
        if nome.lower() == 'sair':
            break
        
        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f'Nota {i} de {nome}: '))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print('Nota deve estar entre 0 e 10.')
                except ValueError:
                    print('Entrada inválida. Digite um número.')
        
        media = sum(notas) / 3
        alunos.append([nome, notas, media])
    return alunos

def mostrar_boletim(alunos):
    print('\nBoletim:')
    print(f'{"Nº":<4} {"Aluno":<20} {"Média":>6}')
    print('-' * 32)
    for i, aluno in enumerate(alunos):
        print(f'{i:<4} {aluno[0]:<20} {aluno[2]:>6.2f}')

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
                print(f'\nNotas de {aluno[0]}:')
                print(f'  NOTA 1: {aluno[1][0]}')
                print(f'  NOTA 2: {aluno[1][1]}')
                print(f'  NOTA 3: {aluno[1][2]}')
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