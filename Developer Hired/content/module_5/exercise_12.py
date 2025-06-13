km = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias alugado: '))
pagar = (dias*90) + (km*0.29)

print(f'Você alugou o carro por {dias}  dias e percorreu {km}km.')
print(f'Preço total a pagar: R${pagar}.')