'''
4.1 - 1. Desenhe um diagrama da pilha que mostre o estado do programa
enquanto executa circle (bob, radius). Você pode fazer a aritmética à
mão ou acrescentar instruções print ao código.

Solução:

__main__

print

polygon
'''



import turtle

# polygon receives an turtle object, te side length
# and the number of sides, and make a polygon
def polygon(t, length, n):

    for i in range(n):
        t.fd(length)
        t.lt(360/n)

# That creates an Turtle object called bob
bob = turtle.Turtle()

length = 200
n = 6

# Opens a window where will show the polygon
print(polygon(bob, length, n))

# Wait for the user close the windown 
turtle.mainloop()