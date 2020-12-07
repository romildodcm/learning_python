# return the initial

# This function will return the first initial of a name
def get_initial(name):
    return name[0:1].upper()

f_name_i = get_initial(input('Enter your first name: '))
m_name_i = get_initial(input('Enter your middle name: '))
l_name_i = get_initial(input('Enter your last name: '))

print(f'Your initials are: {f_name_i}, {m_name_i} and {l_name_i}')
