# Conditional logic

# > Greater than
# < Lass than
# >= Greater than or equal to
# <= Less than or equal to
# == is equal to
# != is not equal to

price = float(input('How much did you pay? '))

if price >= 1.00:
    tax = 0.07*price
else:
    tax = 0.

print(f'Price: {str(price)}, Tax rate5: {str(tax)}')