# superclass file

class Pet:
    def __init__(self, n, c): # initializes the class
        self.__name = n # initial name
        self.__colour = c # the initial colour

    def getName(self):
        return(self.__name)

    def setName(self):
        self.__name = n

    def getColour(self):
        return(self.__colour)

    def setColour(self):
        self.__filled = c

    def __str__(self): # prints out a string
        return('name: ' + self.__name + ' and colour: ' + str(self.__colour))