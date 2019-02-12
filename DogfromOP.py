# Dog subclass
# references the ObjectPet superclass

from ObjectPet import Pet

class Dog(ObjectPet):
    def __init__(self, s, e): # initializers
        super().__init__() # the superclass
        self.__sound = s
        self.__ears = e

    def getSound(self):
        return(self.__sound)

    def setSound(self):
        self.__sound = s

    def getEars(self):
        return(self.__ears)

    def setEars(self):
        self.__ears = e

    def __str__(self):
        return(super().__str__() + " sound: " + str(self.__sound) + " ear type: " + str(self.__ears))