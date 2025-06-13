from random import randint

random_1 = randint(0,10)
random_2 = randint(0,10)
random_3 = randint(0,10)
random_4 = randint(0,10)

numbers = (random_1,random_2,random_3,random_4)
biggest = max(numbers)
smallest = min(numbers)

print(f'Os valores sorteados foram: {numbers}.')
print(f'O maior valor é: {biggest}.')
print(f'O menor valor é:{smallest}.')