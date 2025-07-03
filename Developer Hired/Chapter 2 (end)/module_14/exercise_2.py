
def ambos(largura,comprimento):
    area = largura*comprimento
    return area

largura = float(input('Informe a largura: '))
comprimento = float(input('Informe o comprimento: '))

area = ambos(largura,comprimento)
print(f'O valor da área é de: {area}m²')
