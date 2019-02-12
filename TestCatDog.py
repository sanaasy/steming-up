# multiple inheritance is possible in Python

from CatfromOP import Cat
from DogfromOP import Dog

def main():
    # assignment operation to the variable circle
    c = Cat('meow', 'meat eaters')  # input the radius that is desired
    print('This animal is a', c)
    print('The radius is', circle.getRadius()) # referencing getRadius function
    print('The area is', circle.getArea()) # prints out the circle's area
    print('The diameter is', circle.getDiameter()) # prints out circle's diameter
    print('The perimeter is', circle.getPerimeter()) # print out circle's perimeter

    # we can inherit multiple classes
    # this is called multiple inheritance

    rectangle = Rectangle(2, 4) # takes 2 arguments: one for height, one for width
    print('A rectangle', rectangle)
    print('The width is', rectangle.getWidth()) # prints out rectangle's width
    print('The height is', rectangle.getHeight()) # prints out rectangle's height
    print('The area is', rectangle.getArea()) # prints out rectangle's area
    print('The perimeter is', rectangle.getPerimeter()) # prints out rectangle's perimeter

main()