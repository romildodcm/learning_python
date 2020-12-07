import turtle
from math import pi

# circle receives an turtle object and the radio,
# and makes a circle
def circle(t, r):
    circumference = 2*pi*r
    n = round(circumference/3)+1
    length = circumference/n
    
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

# That creates an Turtle object called bob
bob = turtle.Turtle()

radio = 200

# Opens a window where will show the circle
print(circle(bob, radio))

# Wait for the user close the windown 
turtle.mainloop()