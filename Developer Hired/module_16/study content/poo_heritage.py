class Pessoa:

    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def comer(self):
        print(f'{self.nome} está comendo.')

class Aluno(Pessoa):
    
    @staticmethod
    def estudar():
        print('O(A) aluno(a) está estudando.')

class Professor(Pessoa):

    @staticmethod
    def ensinar():
        print('O(A) professor(a) está ensinando.')


aluno = Aluno(nome='Ana',cpf='181')
print('Dados do aluno:')
print(aluno.nome)
print(aluno.cpf)
aluno.comer()
aluno.estudar()

print('*'*50)

professor = Professor(nome='Israel',cpf='094')
print('Dados do professor:')
print(professor.nome)
print(professor.cpf)
professor.comer()
professor.ensinar()