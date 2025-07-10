class Selecao:
    def __init__(self):
        self.nome = ""
        self.partidas = 0
        self.gols = []
        self.total = 0

    def ler_dados(self):
        self.nome = input('Nome da seleção: ').strip()

        while True:
            try:
                self.partidas = int(input('Quantas partidas jogou na Copa de 2002? '))
                if self.partidas < 0:
                    print('Número de partidas não pode ser negativo.')
                    continue
                break
            except ValueError:
                print('Digite um número inteiro válido.')

        for i in range(1, self.partidas + 1):
            while True:
                try:
                    gol = int(input(f'Gols feitos na partida {i}: '))
                    if gol < 0:
                        print('Quantidade de gols não pode ser negativa.')
                        continue
                    self.gols.append(gol)
                    break
                except ValueError:
                    print('Digite um número inteiro válido.')

        self.total = sum(self.gols)

    def mostrar_dados(self):
        print(f'\nDesempenho da seleção {self.nome}:')
        for i, g in enumerate(self.gols, start=1):
            print(f'--> Na partida {i}, foram {g} gols')
        print(f'\nFoi um total de {self.total} gols na Copa do Mundo de 2002')