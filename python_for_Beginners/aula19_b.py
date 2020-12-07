# String comparisons are case sensitive
# "Canada" é diferente de "CANADA"
# So, if i work with string comparison, it's necessary format
# the string before comparison, follow this example

country = input('Where are you from? ')

if country.capitalize() == 'Canada':
    print('Oh, look a Canadian!')
else:
    print('You are not from Canada!')