# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you
values = [1, 2, 3]


def calculate_average(values):
    lst = []
    sum_values = sum(values)
    average = sum_values/len(values)
    lst.append(average)
    return lst


print(calculate_average(values))
