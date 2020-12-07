'''
A function object is a value that can be assigned to a variable or passed as an argument. For example, do_twice is a function which takes a function object as an argument and calls this two times:
'''

def do_twice(f):
    f()
    f()

'''
An example that uses do_twice to call a function called print_spam twice:
'''

def print_spam():
    print("spam")

do_twice(print_spam)

