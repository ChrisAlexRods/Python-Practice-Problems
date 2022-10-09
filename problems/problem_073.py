# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.
class Student():
    def __init__(self, name):
        self.name = name
        self.score = []

    def add_score(self, score):
        self.score.append(score)

    def average(self,):
        if len(self.score) == 0:
            return None
        average = sum(self.score) / len(self.score)
        return average

student = Student("Malik")

print(student.average())    # Prints None
student.add_score(80)
print(student.average())    # Prints 80
student.add_score(90)
student.add_score(82)
print(student.average())    # Prints 84
