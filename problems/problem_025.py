# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    if len(values) == 0:
        return None
    list = 0

    for items in values:
        list = list + items
    return list


print(calculate_sum([5 , 5, 5]))
