total = 0
maior_750 = 0
contador = 0
preco_barato = 0
nome_barato = ''

while True:
    produto = str(input('\nNome do produto: '))
    preco = float(input('Preço do produto: '))

    total += preco

    if preco > 750:
        maior_750 += 1

    contador += 1
    if contador == 1 or preco < preco_barato:
        preco_barato = preco
        nome_barato = produto

    continuar = str(input('Gostaria de continuar? [S/N] ')).strip().upper()
    while continuar not in ('N', 'S'):
        continuar = str(input('Gostaria de continuar? [S/N] ')).upper()

    if continuar == 'N':
        break

print(f'\nO total da compra foi de R${total:.2f}.')
print(f'Temos {maior_750} produto(s) que custam mais de R$750,00.')
print(f'O produto mais barato foi {nome_barato.title()}, que custa R${preco_barato:.2f}.')