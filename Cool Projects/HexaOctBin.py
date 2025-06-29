number = int(input('Enter a number: '))

print('''
[1] - Convert to Binary
[2] - Convert to Octal
[3] - Convert to Hexadecimal
''')

option = int(input('Choose a conversion option: '))

if option == 1:
    binary = bin(number)
    print(f'The number {number} converted to binary is: {binary}.')
elif option == 2:
    octal = oct(number)
    print(f'The number {number} converted to octal is: {octal}.')
elif option == 3:
    hexadecimal = hex(number)
    print(f'The number {number} converted to hexadecimal is: {hexadecimal}.')
else:
    print('Please enter a valid option.')
