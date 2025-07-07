def aumentar(preco):
    aumento = preco + preco / 100*10
    return aumento


def diminuir(preco):
    desconto = preco - preco / 100*10
    return desconto

def  dobrar(preco):
    dobro = preco*2
    return dobro

def cortar(preco):
    metade = preco/2
    return metade

preco = float(input('Digite um preco: '))
aumento = aumentar(preco)
desconto = diminuir(preco)
dobro = dobrar(preco)
metade = cortar(preco)
print(f'O preço com 10% de aumento é: R${aumento}.')
print(f'O preço com 10% de desconto é: R${desconto}.')
print(f'O dobro de R${preco} é: R${dobro}.')
print(f'A metade de R${preco} é: R${metade}.')