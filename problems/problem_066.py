# Write a class that meets these requirements.
#
# Name:       Book
#
# Required state:
#    * author name, a string
#    * title, a string
#
# Behavior:
#    * get_author: should return "Author: «author name»"
#    * get_title:  should return "Title: «title»"
#
# Example:
#    book = Book("Natalie Zina Walschots", "Hench")
#
#    print(book.get_author())  # prints "Author: Natalie Zina Walschots"
#    print(book.get_title())   # prints "Title: Hench"
#
# There is pseudocode availabe for you to guide you


# class Book
    # method initializer method with required state
    # parameters author and title
        # set self.author = author
        # set self.title = title

    # method get_author(self)
        # returns "Author: " + self.author

    # method get_title(self)
        # returns "Title: " + self.title
# defines the class
class Book:
    #function with self and the 2 paramaters asked above
    def __init__(self, author, title):
        #becuase it's a class you have to do self.paramter = paramteter
        self.author = author
        self.title = title
#for the second function you have to add self to the parameters
# the return is combining the string author and the input of the user for the actual name
    def get_author(self):
        return "author " + self.author
# another function. alwys keep the self. This time we're combing the "title" string and user input
    def get_title(self):
        return "title " + self.title
#one of the more annoying thins is making a variable to pass through all these functions
#to call upon it you make a varaible
# = to CLASSNAME(PARAMETER1, PARAMTER2)
#then do the print statement
hp = Book("Jk Rowling", "Harry Potter")
print(hp.get_author())
print(hp.get_title())