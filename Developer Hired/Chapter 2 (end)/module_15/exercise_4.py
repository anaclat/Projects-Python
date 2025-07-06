frase = input('Digite uma frase: ').lower()

def verificar_frase(frase):
    letra_i = frase.count('i')
    print(f'A letra "i" aparece {letra_i} vez(es) na sua frase.')

    if letra_i != 0:
        print(f'A primeira letra "i" aparece na {frase.find('i')} posição.')
        print(f'A última letra "i" aparece na {frase.rfind('i')} posição.')

verificar_frase(frase)