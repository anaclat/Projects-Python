# função

def printar_tracinhos(): # função sem parâmetro
    print('=========')

printar_tracinhos()

#########################################
def escrever_nome_formatado(nome): # função com 1 parâmetro
    print(f'Meu nome é {nome}.')

escrever_nome_formatado('ana')

#########################################
def somar(numero_1, numero_2): # função de 2 ou mais parâmetros
    resultado = numero_1 + numero_2
    print(resultado)

somar(3,6)

#########################################
def saudar(nome,mensagem='Bom dia'): #função com parâmetro default
    print(f'Olá, {nome}! {mensagem}')

saudar('Ana')
saudar('Ana', mensagem='Boa Tarde!')

#########################################

def calcular_media(nota_1,nota_2):
    media = (nota_1 + nota_2)/2
    return media

def verificar(media):
    if media >=7:
        print(f'Você está APROVADO.')
    else:
        print(f'Você está REPROVADO.')

media = calcular_media(9,4)
verificar(media)