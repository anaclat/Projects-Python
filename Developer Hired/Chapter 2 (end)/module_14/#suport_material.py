# função

def printar_tracinhos(): # função sem parâmetro
    print('=========')

printar_tracinhos()

def escrever_nome_formatado(nome): # função com 1 parâmetro
    print(f'Meu nome é {nome}.')

escrever_nome_formatado('ana')

def somar(numero_1, numero_2):
    resultado = numero_1 + numero_2
    print(resultado)

somar(3,6)