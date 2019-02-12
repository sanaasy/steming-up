# polymorphism example

from CircleFromGO import Circle
from RectangleFromGO import Rectangle

def main():
    # display the circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    displayObject(c)
    displayObject(r)
    print('Are the circle and rectangle the same size?', isSameArea(r, c))

# display the geometric object properties
def displayObject(g):
    print(g.__str__())

# compare the areas of the two geometric objects
def isSameArea(g1, g2):
    return(g1.getArea() == g2.getArea())

main()


