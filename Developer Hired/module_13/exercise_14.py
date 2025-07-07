maior_20 = 0
mulher = 0
homens_menor_35 = 0

while True:
    idade = int(input('\nInforme a sua idade: '))
    genero = str(input('Informe o seu gênero [F/M]: ')).upper()
    while genero not in ('M', 'F'):
        genero = str(input('Informe o seu gênero [F/M]: ')).upper()

    if idade > 20:
        maior_20 += 1

    if genero == "F":
        mulher += 1

    if idade < 35 and genero == 'M':
        homens_menor_35 += 1

    continuar = str(input('Gostaria de continuar? [S/N] ')).upper()
    while continuar not in ('N', 'S'):
        continuar = str(input('Gostaria de continuar? [S/N] ')).upper()

    if continuar == 'N':
        print(f'\nTotal de pessoas com mais de 20 anos: {maior_20}.')
        print(f'Ao todo temos {mulher} mulher(es) cadastradas.')
        print(f'Temos {homens_menor_35} homem(s) com menos de 35 anos.')
        break