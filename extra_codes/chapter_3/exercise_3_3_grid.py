'''
The exercise was more simple, but I wanted to make a general function
that creates an ASCII matrix with the input of lines and columns.

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''

'''
A function to make the horizontal grid:
"+ - - - - + - - - - +..."
'''
def horizontal_grid(total_columns):
    for i in range(total_columns):
        print('+', end=' ')
        for n in range(4):
            print('-', end=' ')
    print('+')

'''
A function to make the vertical grid:
"|         |         |..."
'''
def vertical_grid(total_columns):
    for i in range(total_columns):
        print('|         ', end="")
    print('|')

'''
A function to runs n times a function with an argument,
in this case, used to make the vertical grids.
'''
def do_n(n, f, argument):
    for i in range(n):
        f(argument)

'''
Makes the grids with the number of columns and lines,
and the previous functions.
'''
def grid_maker(columns, lines):
    for i in range(lines):
        horizontal_grid(columns)
        do_n(4, vertical_grid, columns)
    horizontal_grid(columns)

l = int(input("Line number: "))
c = int(input("Column number: "))

grid_maker(c, l)