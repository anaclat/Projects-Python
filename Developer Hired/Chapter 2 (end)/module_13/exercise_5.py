numero = int(input('Quantos números você quer ver? '))

contador = 3
primeiro_termo = 0
segundo_termo = 1

print(primeiro_termo)
print(segundo_termo)

while contador <= numero:
    terceiro_termo = primeiro_termo + segundo_termo
    print(terceiro_termo)
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    contador += 1