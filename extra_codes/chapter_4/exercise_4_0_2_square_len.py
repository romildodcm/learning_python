import turtle

# square receives an turtle object and the length, and make a square
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# That creates an Turtle object called bob
bob = turtle.Turtle()

length = 50

# Opens a window where will show the square
print(square(bob, length))

# Wait for the user close the windown 
turtle.mainloop()