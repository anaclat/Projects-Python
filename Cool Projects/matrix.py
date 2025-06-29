def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

rows = get_int("Enter the number of rows: ")
columns = get_int("Enter the number of columns: ")

matrix = [[0 for _ in range(columns)] for _ in range(rows)]

for row in range(rows):
    for column in range(columns):
        value = get_int(f"Enter a value for ROW {row}, COLUMN {column}: ")
        matrix[row][column] = value

print("\nResulting Matrix:")
for row in matrix:
    for value in row:
        print(f"{value:^7}", end="")  
    print()
