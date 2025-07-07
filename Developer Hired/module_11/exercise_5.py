matriz = [
[0, 0],
[0, 0]
]


for coluna in range(0,  2):
    for linha in range(0, 2):
         numero = int(input(f'Digite um valor para a COLUNA {coluna} e LINHA {linha}: '))
         matriz[linha] [coluna] = numero

for linha in matriz:
    print(linha)