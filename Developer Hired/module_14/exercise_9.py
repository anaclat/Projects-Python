def formatar_moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def aumentar(preco, formatar=False):
    aumento = preco + preco * 0.10
    return formatar_moeda(aumento) if formatar else aumento

def diminuir(preco, formatar=False):
    desconto = preco - preco * 0.10
    return formatar_moeda(desconto) if formatar else desconto

def dobrar(preco, formatar=False):
    dobro = preco * 2
    return formatar_moeda(dobro) if formatar else dobro

def cortar(preco, formatar=False):
    metade = preco / 2
    return formatar_moeda(metade) if formatar else metade

preco = float(input('Digite um preço: R$'))

aumento = aumentar(preco, formatar=True)
desconto = diminuir(preco, formatar=True)
dobro = dobrar(preco, formatar=True)
metade = cortar(preco, formatar=True)

print(f'O preço com 10% de aumento é: {aumento}.')
print(f'O preço com 10% de desconto é: {desconto}.')
print(f'O dobro de R${preco:.2f} é: {dobro}.')
print(f'A metade de R${preco:.2f} é: {metade}.')