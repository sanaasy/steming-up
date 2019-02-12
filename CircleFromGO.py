# circle from geometric object
# import the superclass

from GeometricObject import GeometricObject
# from file name  import class

import math

class Circle(GeometricObject):
    # initialize the class
    def __init__(self, radius):
        super().__init__() # referencing the initializer from the superclass
        self.__radius = radius

    def getRadius(self):
        return(self.__radius)

    def setRadius(self):
        self.__radius = radius

    def getArea(self):
        return(self.__radius * self.__radius * math.pi)

    def getDiameter(self):
        return(2 * self.__radius)

    def getPerimeter(self):
        return(2 * self.__radius * math.pi)

    def printCircle(self):
        print(self.__str__() + 'radius:' + str(self.__radius))

print(Circle(GeometricObject)) # call the function