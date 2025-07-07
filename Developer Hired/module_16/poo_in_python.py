class Abada:

    def  __init__(self):

    # CARACTERÍSTICAS / ATRIBUTOS
        self.cor = None
        self.tamanho = None
        self.tecido = None
        self.nome_festa = None

    # ESTADOS / ATRIBUTOS
        self.limpo = True
        self.bonito = True

    # MÉTODOS / ATRIBUTOS
    def vestir(self):
        print(f'Estou vestindo o meu ABADÁ...')

    def rasgar(self):
        print('Estou rasgando o meu ABADÁ...')

    def bordar(self):
        print('Estou bordando o meu ABADÁ...')


objeto_abada_1  = Abada()
objeto_abada_1.cor = 'Azul'
objeto_abada_1.tamanho = 'P'
objeto_abada_1.tecido = 'Cetim'
objeto_abada_1.nome_festa =  'Feijoada do Cacau'


print(f'OBJETO ABADA 1: {objeto_abada_1}.')
print(f'Cor: {objeto_abada_1.cor}.')
print(f'Tamanho: {objeto_abada_1.tamanho}.')
print(f'Tecido: {objeto_abada_1.tecido}.')
print(f'Nome da festa: {objeto_abada_1.nome_festa}.')
print(f'Limpo: {objeto_abada_1.limpo}.')
print(f'Bonito: {objeto_abada_1.bonito}.')

print('*'  * 80)

objeto_abada_2  = Abada()
objeto_abada_2.cor = 'Vermelho'
objeto_abada_2.tamanho = 'M'
objeto_abada_2.tecido = 'Lã'
objeto_abada_2.nome_festa =  'Carnaval 2025'


print(f'OBJETO ABADA 2: {objeto_abada_2}.')
print(f'Cor: {objeto_abada_2.cor}.')
print(f'Tamanho: {objeto_abada_2.tamanho}.')
print(f'Tecido: {objeto_abada_2.tecido}.')
print(f'Nome da festa: {objeto_abada_2.nome_festa}.')
print(f'Limpo: {objeto_abada_2.limpo}.')
print(f'Bonito: {objeto_abada_2.bonito}.')

objeto_abada_2.vestir()