# cat from object pet
# import the superclass

from ObjectPet import Pet

class Cat(ObjectPet):
    # initialize the class
    def __init__(self, s, f):
        super().__init__() # referencing the initializer from the superclass
        self.__sound = s

    def getSound(self):
        return(self.__sound)

    def setSound(self):
        self.__sound = s

    def getFood(self):
        return(self.__food)

    def setFood(self):
        self.__food = f

    def printCat(self):
        print(self.__str__() + 'sound:' + str(self.__sound) + 'food:' + str(self.__food))

print(Cat(ObjectPet)) # call the function