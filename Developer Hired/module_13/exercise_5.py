numero = int(input('Quantos números você quer ver? '))

contador = 3
primeiro_termo = 0
segundo_termo = 1

print(primeiro_termo, end=' ')
print(segundo_termo, end=' ')

while contador <= numero:
    terceiro_termo = primeiro_termo + segundo_termo
    print(terceiro_termo, end=' ')
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    contador += 1