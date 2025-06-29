from random import randint

moves = ('ROCK', 'PAPER', 'SCISSORS')
computer = randint(0, 2)

print('''
Let's play:
      [0] ROCK
      [1] PAPER
      [2] SCISSORS
''')

user = int(input('Make your move: '))


if user not in [0, 1, 2]:
    print('INVALID OPTION!')
else:
    print(f'The computer chose {moves[computer]} and you chose {moves[user]}.')

    if computer == 0:  
        if user == 0:
            print('IT\'S A TIE.')
        elif user == 1:
            print('YOU WIN.')
        elif user == 2:
            print('THE COMPUTER WINS.')

    elif computer == 1: 
        if user == 1:
            print('IT\'S A TIE.')
        elif user == 2:
            print('YOU WIN.')
        elif user == 0:
            print('THE COMPUTER WINS.')

    elif computer == 2:  
        if user == 2:
            print('IT\'S A TIE.')
        elif user == 0:
            print('YOU WIN.')
        elif user == 1:
            print('THE COMPUTER WINS.')