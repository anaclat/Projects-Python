total = 0
over_750 = 0
counter = 0
cheapest_price = 0
cheapest_product = ''

while True:
    product = str(input('\nProduct name: '))
    price = float(input('Product price: $'))

    total += price

    if price > 750:
        over_750 += 1

    counter += 1
    if counter == 1 or price < cheapest_price:
        cheapest_price = price
        cheapest_product = product

    continue_input = str(input('Do you want to continue? [Y/N] ')).strip().upper()
    while continue_input not in ('Y', 'N'):
        continue_input = str(input('Do you want to continue? [Y/N] ')).strip().upper()

    if continue_input == 'N':
        break

print(f'\nThe total purchase amount was ${total:.2f}.')
print(f'There are {over_750} product(s) costing more than $750.00.')
print(f'The cheapest product was {cheapest_product.title()}, which costs ${cheapest_price:.2f}.')