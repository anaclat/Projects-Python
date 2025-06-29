from time import sleep

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

while True:
    print('''
    Choose an option:
        [1] add
        [2] multiply
        [3] greater and smaller
        [4] change numbers
        [5] exit the program
''')

    option = int(input('What is your option? '))

    if option == 1:
        addition = first_number + second_number
        print(f'The result of {first_number} + {second_number} is: {addition}.')
    
    elif option == 2:
        multiplication = first_number * second_number
        print(f'The result of {first_number} x {second_number} is: {multiplication}.')

    elif option == 3:
        if second_number > first_number:
            print(f'{second_number} is greater than {first_number}.')
        elif second_number < first_number:
            print(f'{first_number} is greater than {second_number}.')
        else:
            print('The numbers are equal.')

    elif option == 4:
        print('Enter new numbers...')
        first_number = int(input('Enter the first number: '))
        second_number = int(input('Enter the second number: '))

    elif option == 5:
        print('Exiting...')
        sleep(2)
        print('Program ended.')
        break

    else:
        print('Please enter a valid option!')