import time
import os
from random import choice
from colorama import init, Fore, Style

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_pergunta():
    while True:
        pergunta = input(Fore.CYAN + '🎤 Faça sua pergunta à Bola 8 Mágica (ou digite "sair"): ').strip()
        if pergunta:
            return pergunta
        print(Fore.YELLOW + "⚠️ Você precisa digitar uma pergunta!")

def gerar_resposta():
    respostas = [
        "Com certeza!",
        "Sem dúvida alguma.",
        "Sim, definitivamente.",
        "É provável que sim.",
        "As perspectivas são boas.",
        "Concentre-se e pergunte novamente.",
        "Melhor não te contar agora.",
        "Não conte com isso.",
        "Minhas fontes dizem que não.",
        "Muito duvidoso.",
        "A resposta é complicada, tente mais tarde.",
        "Não tenho uma resposta para isso no momento."
    ]
    return choice(respostas)

def bola_oito_magica():
    limpar_tela()
    print(Fore.MAGENTA + Style.BRIGHT + "🎱 Bem-vindo(a) à Bola 8 Mágica!")
    print('-' * 40)

    while True:
        pergunta = obter_pergunta()

        if pergunta.lower() in ('sair', 'exit', 'quit'):
            print(Fore.GREEN + "\n👋 Obrigado por usar a Bola 8 Mágica! Até a próxima.")
            break

        print(Fore.BLUE + "🔮 Pensando...")
        time.sleep(2)  

        resposta = gerar_resposta()
        print(Fore.MAGENTA + f'🎱 Resposta: {resposta}\n')
        time.sleep(1.5)

bola_oito_magica()
