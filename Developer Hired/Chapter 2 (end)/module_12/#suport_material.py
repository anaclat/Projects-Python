# IF

a = 0

if a == 1:
    print('a é igual a 1.')
else:
    print('a não é igual a 1.')

############################################

b = 4

if b == 4:
    print('b é igual a 4.')

if b != 4:
    print('b é diferente de 4.')

if b > 4:
    print('b é maior que quatro.')

if b < 4:
    print('b é menor que 4.')

if b >= 4:
    print('b é maior ou igual a 4.')

if b <= 4:
    print('b é menor ou igual a 4.')

if b < 4 and b > 0:
    print('b é maior que 0 E menor que 4.')

if b == 2 or b== 1:
    print('b é igual a 2 OU igual a 1.')

if b in (1,2):
    print('b é igual a 2 OU igual a 1.')

if b not in (1,2,3,4):
    print('b não é igual a 1,2,3 ou 4')

if b == 1:
    print('b é igual a 1.')
elif b ==2:
    print('b é igual a 2.')
else:
    print('b não é 1 nem 2.')