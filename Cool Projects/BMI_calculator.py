weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

bmi = weight / (height ** 2)

print(f'Your BMI is: {bmi}.')

if bmi < 18.5:
    print('You are under your ideal weight.')
elif 18.5 <= bmi < 25:
    print('You are at your ideal weight. Congratulations!')
elif 25 <= bmi < 30:
    print('You are overweight.')
elif 30 <= bmi < 40:
    print('You are obese.')
else:
    print('You have morbid obesity. WARNING!!!')