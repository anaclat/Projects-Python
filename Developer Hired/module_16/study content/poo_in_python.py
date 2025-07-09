from datetime import date

class Abada:

    dia_de_hoje = date.today()

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
    # MÉTODO DE INSTÂNCIA (SELF)
    def vestir(self):
        if self.limpo is True:
            print(f'Estou vestindo o meu ABADÁ...')
        else:
            print(f'Não vista o ABADÁ da festa {self.nome_festa}')

    # MÉTODO DE CLASSE
    @classmethod
    def sujar(cls):
        print('Estou sujando o meu ABADÁ...')

    # MÉTODO ESTÁTICO
    @staticmethod
    def cortar():
        print('Estou cortando o meu ABADÁ...')


print(Abada.dia_de_hoje)

# INSTÂNCIA
objeto_abada  = Abada()
objeto_abada.nome_festa = 'Feijoada da Ana.'
objeto_abada.limpo = False
objeto_abada.vestir()

# CLASSE
Abada.sujar()

# ESTÁTICO
objeto = Abada()
objeto.cortar()
Abada.cortar()