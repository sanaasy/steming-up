# Rectangle subclass
# references the GeometricObject superclass

from GeometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, width = 1, height = 1): # initializers
        super().__init__() # the superclass
        self.__width = width
        self.__height = height

    def getWidth(self):
        return(self.__width)

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return(self.__height)

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return(self.__width * self.__height)

    def getPerimeter(self):
        return(2 * (self.__width + self.__height))

# overriding __str__ in the GeometricObject superclass
    def __str__(self):
        return(super().__str__() + " width: " + str(self.__width) + " height: " + str(self.__height))