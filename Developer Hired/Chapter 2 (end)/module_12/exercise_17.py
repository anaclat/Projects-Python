palavras = ('aprender', 'programar', 'linguagem', 'mercado', 'praticar')

for palavra in palavras:
    contador_vogais = 0
    print(f'Na palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
            contador_vogais += 1
            print(letra, end=' ')
    print(f'\nTotal de {contador_vogais} vogais nesta palavra.\n')