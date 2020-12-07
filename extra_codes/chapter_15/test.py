class Point:
    """represents a point in 2-D space"""
    def print_point(self):
        print('(%g, %g)' %(self.x, self.y))

blank = Point()
blank.x = 2.0
blank.y = 4.0

print(blank.x)
print(blank.y)

blank.print_point()

