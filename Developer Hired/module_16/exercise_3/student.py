class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        self.media = 0.0

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            raise ValueError('Nota fora do intervalo permitido.')

    def calcular_media(self):
        if len(self.notas) == 3:
            self.media = sum(self.notas) / 3
        else:
            raise ValueError('Número de notas insuficiente para calcular média.')