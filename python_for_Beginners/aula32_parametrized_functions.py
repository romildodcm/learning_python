
# The parametrized function have the force_uppercase parameter
# Without standard value, the line code would be like the next line
# def get_initial(name, force_uppercase):

# and in this example True is the standard value for the force_uppercase parameter
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        out = name[0:1].upper()
    else:
        out = name[0:1]
    return out

name = input('Enter your first name: ')

# we have any ways to use parametrized functions, follow the examples

# in the get_initial function we do not set the parameter
# in this case the parameter will be the standard, that in this case is True
print(f'Name: {name} \nInitial: {get_initial(name)}')
# If I don't set the standard parameter, I need to set like this
print(f'Name: {name} \nInitial: {get_initial(name, True)}')
# in this sample, the get_initial function have the parameter = False in order
print(f'Name: {name} \nInitial: {get_initial(name, False)}')
# If I know the parameters but don't remenber the order, I can set like this example
print(f'Name: {name} \nInitial: {get_initial(force_uppercase = False, name = name)}')



