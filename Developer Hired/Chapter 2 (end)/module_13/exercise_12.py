while True:
    contador = 1
    tabuada = int(input('Quer ver a tabuada de qual número? '))

    if tabuada < 0:
        print('Programa encerrado.')
        break

    while contador < 11:
        print(f'{tabuada}  X {contador} = {contador*tabuada}.')
        contador +=1