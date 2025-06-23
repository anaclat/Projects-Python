reta_um = float(input('Digite o valor da reta um: '))
reta_dois = float(input('Digite o valor da reta dois: '))
reta_tres = float(input('Digite o valor da reta três: '))
retas = reta_um, reta_dois, reta_tres

if reta_um < (reta_dois + reta_tres) and reta_dois < (reta_tres + reta_um) and reta_tres < (reta_um + reta_dois):
    print(f'O triângulo com as retas {retas} é válido.')
else:
    print(f'O triângulo com as retas {retas} é inválido.')