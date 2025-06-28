while True:
    bebeu = str(input('Você já bebeu água hoje? [Sim/Não] '))

    if bebeu == 'Sim':
        print('Ótimo!')
        break
    elif bebeu == 'Não':
        print('Vá beber!')
    else:
        print('Não entendi sua resposta. ')