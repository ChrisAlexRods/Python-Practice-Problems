# Write a function that meets these requirements.
#
# Name:       remove_duplicates
# Parameters: a list of values
# Returns:    a copy of the list removing all
#             duplicate values and keeping the
#             original order
#
# Examples:
#     * input:   [1, 1, 1, 1]
#       returns: [1]
#     * input:   [1, 2, 2, 1]
#       returns: [1, 2]
#     * input:   [1, 3, 3, 20, 3, 2, 2]
#       returns: [1, 3, 20, 2]
numbers = [1, 2, 2, 1]
def remove_duplicates(numbers):
    lst = []
    # the question is calling for a copy of a list so we need a empty list
    for number in numbers:
        #plural of the parameter above
        if number not in lst:
            # the big thing here is the "in". If a number isn't in the list function then add it
            # IF it already is then the the function will get rid of it
            lst.append(number)
            #the process of appending the number into the lst
    return lst
    #returning the list

print(remove_duplicates(numbers))
