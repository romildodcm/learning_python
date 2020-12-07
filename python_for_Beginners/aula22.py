# Multiple conditions

print('----------------------------------------\n### Welcome to Canada Tax Calculator ###')

country = input('What country do you live in? ')
tax = 0

if country.capitalize() == 'Canada':
    print('----------------------------------------')
    province = input('What province/state do you live in? ')
    province = province.capitalize()
#   The first type of conditions with 'or'
#   if province == 'Alberta' or province == 'Nunavut':
#   Another type is the contition with list:
    if province in('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.07
    print('----------------------------------------')
    print(f'For {province} the tax is {str(tax)}')
else:
    tax = 0
    print('----------------------------------------')
    print(f'You are from {country} the tax is {str(tax)}')
print('----------------------------------------')

