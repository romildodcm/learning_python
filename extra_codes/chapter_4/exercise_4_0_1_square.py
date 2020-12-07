import turtle

# square receives an turtle object and make a square
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# That creates an Turtle object called bob
bob = turtle.Turtle()

# Opens a window where will show the square
print(square(bob))

# Wait for the user close the windown 
turtle.mainloop()