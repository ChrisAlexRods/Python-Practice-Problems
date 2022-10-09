# Write a class that meets these requirements.
#
# Name:       Employee
#
# Required state:
#    * first name, a string
#    * last name, a string
#
# Behavior:
#    * get_fullname: should return "«first name» «last name»"
#    * get_email:    should return "«first name».«last name»@company.com"
#                    all in lowercase letters
#
# Example:
#    employee = Employee("Duska", "Ruzicka")
#
#    print(employee.get_fullname())  # prints "Duska Ruzicka"
#    print(employee.get_email())     # prints "duska.ruzicka@company.com"
#
# You may want to look at the ".lower()" method for strings to
# help with this code.
#
# There is pseudocode availabe for you to guide you


# class Employee
    # method initializer method with required state
    # parameters first name and last name
        # set self.first_name = first_name
        # set self.last_name = last_name

    # method get_fullname(self)
        # returns self.first_name + " " + self.last_name

    # method get_email(self)
        # returns self.first_name.lower() + "." + self.last_name.lower()
        #         + "@company.com"
# making the class
class Employee():
   #for the function we are establishing our parameters and  = self.parameter
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
#  for the first second  function we're combining the two strings of data we recive from the user
#It's gotta specify the self version of the paramters or the function won't identify them
    def full_name(self):
        return self.first_name + " " + self.last_name
# for the email we're doing the same thing except it's supposed to be lower
# to do this we append the .lower method to make sure our variable is always lower case
# then we're adding a string at the end to complete the email
    def email(self):
        return self.first_name.lower() + self.last_name.lower() + "@company.com"
#we have to make a variable equal to the = Class(PARAMETER1, PARAMETER2)
chris = Employee("chris", "rod")
#because we're testing each function we have to print each specific function
print(chris.full_name())
print(chris.email())