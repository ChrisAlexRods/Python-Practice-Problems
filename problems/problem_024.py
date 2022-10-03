# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    if len(values) == 0:
        return None
    list = 0
    for items in values:
        list = list + items
    return list/len(values)


print(calculate_average([5, 6 , 7]))
