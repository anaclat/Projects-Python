import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 4
COLS = 4

SYMBOL_COUNT = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

SYMBOL_VALUE = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def deposit() -> int:
    while True:
        amount = input('Enter deposit amount: $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            print('Amount must be greater than 0.')
        else:
            print('Please enter a valid number.')


def get_number_of_lines() -> int:
    while True:
        lines = input(f'Enter number of lines to bet on (1-{MAX_LINES}): ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            print(f'Please enter a number between 1 and {MAX_LINES}.')
        else:
            print('Please enter a valid number.')


def get_bet() -> int:
    while True:
        amount = input(f'Enter your bet per line (${MIN_BET} - ${MAX_BET}): $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            print(f'Bet must be between ${MIN_BET} and ${MAX_BET}.')
        else:
            print('Please enter a valid number.')


def spin_machine(rows: int, cols: int, symbols: dict) -> list[list[str]]:
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns: list[list[str]]):
    print('\nSLOT MACHINE')
    print('-' * (COLS * 4 - 1))
    for row in range(ROWS):
        row_output = ' | '.join(columns[col][row] for col in range(COLS))
        print(' ' + row_output)
    print('-' * (COLS * 4 - 1))


def check_winnings(columns: list[list[str]], lines: int, bet: int, values: dict) -> tuple[int, list[int]]:
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def spin(balance: int) -> int:
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'Insufficient balance. You have: ${balance}')
        else:
            break

    print(f'\nYou are betting ${bet} on {lines} lines. Total bet: ${total_bet}')
    slots = spin_machine(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)
    net_result = winnings - total_bet

    if winnings > 0:
        print(f'You won ${winnings} on lines: {", ".join(map(str, winning_lines))}')
    else:
        print('No winning lines this round.')

    return net_result


def main():
    balance = deposit()

    while True:
        print(f'\nCurrent balance: ${balance}')
        choice = input('Press Enter to play (or "q" to quit): ').strip().lower()

        if choice == 'q':
            break

        if balance < MIN_BET:
            print('You do not have enough to continue playing.')
            break

        balance += spin(balance)

    print(f'\nYou left with ${balance}. Thanks for playing!')


if __name__ == "__main__":
    main()