def contar(inicio,fim,passo):
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}:',end=" ")

    if passo < 1:
     fim -=1
    else:
       fim +=1

    for indice in range(inicio,fim,passo):
        print(indice,end=' ')

contar(1,8,1)
contar(8,0,-2)
contar(1,7,3)

print()