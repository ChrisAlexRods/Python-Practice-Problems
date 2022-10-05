# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
class Animal:
    def __init__(self, number_of_legs, primary_color):
        self.number_of_legs = number_of_legs
        self.primary_color = primary_color

    def describe(self):
        return(self.__class__.__name__+
        "has"
        + str(self.number_of_legs
        +"legs and is primarily" 
        +self.primary_color))

first_animal = Animal(4, "blue")
print(first_animal)
second_animal = Animal(8, "brown")
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
class Dog(Animal):
    def speak(self):
        return "bark"


fido = Dog(4,"pink")
print(fido.describe())
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"

class Cat(Animal):
    def speak(self):
        return "Mew"
catdog = Cat(4,"yellow")
print(catdog.speak())