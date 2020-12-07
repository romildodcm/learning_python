import turtle
from math import pi

# arc receives an turtle object, the radio and the angle,
# and makes a arc
def arc(t, r, angle):
    arc_length = 2*pi*r*angle/360
    n = round(arc_length/3)+1
    step_length = arc_length/n
    step_angle = angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# That creates an Turtle object called bob
bob = turtle.Turtle()

radio = 100
alpha = 340

# Opens a window where will show the arc
print(arc(bob, radio, alpha))

# Wait for the user close the windown 
turtle.mainloop()