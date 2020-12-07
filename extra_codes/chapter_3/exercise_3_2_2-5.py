
'''
This function receives two arguments (a function and a variable)
and runs twice the function with the parameter/variable:
'''
def do_twice(function, argument):
    function(argument)
    function(argument)

'''
A function presented in this chapter for printing twice,
do_twice ismore general than print_twice:
'''
def print_twice(argument):
    print(argument)
    print(argument)

'''
This function uses do_twice twice for runs the function
with the parameter four times:
'''
def do_four(function, argument):
    do_twice(function, argument)
    do_twice(function, argument)

print("do_twice:\n")
do_twice(print, "spam")

print("\ndo_four:\n")
do_four(print, "test")