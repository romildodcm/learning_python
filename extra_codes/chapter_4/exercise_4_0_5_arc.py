import turtle
from math import pi

# arc receives an turtle object, the radio and the angle,
# and makes a arc
def arc(t, r, angle):
    circumference = 2*pi*r
    n = round(circumference/3)+1
    length = circumference/n
    
    for i in range(round(n*(angle/360))):
        t.fd(length)
        t.lt(360/n)

# That creates an Turtle object called bob
bob = turtle.Turtle()

radio = 100
alpha = 340

# Opens a window where will show the arc
print(arc(bob, radio, alpha))

# Wait for the user close the windown 
turtle.mainloop()