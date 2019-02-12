# july 31, 2018
# circle(subclass) from a geometric object(superclass)
# __ syntax before a method hides the information from the subclass

class GeometricObject:
    def __init__(self, colour = 'red', filled = True): # initializes the class
        self.__colour = colour # initial colour
        self.__filled = filled # the initial state of being filled

    def getColour(self):
        return(self.__colour) # returns to me the colour of my object

    def setColour(self):
        self.__colour = colour # change the colour of my object

    def isFilled(self):
        return(self.__filled)

    def getFilled(self):
        self.__filled = filled

    def __str__(self): # prints out a string
        return('colour: ' + str(self.__colour) + ' and filled: ' + str(self.__filled))