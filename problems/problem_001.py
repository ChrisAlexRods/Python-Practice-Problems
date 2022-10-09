# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.
value1 = 10
value2 = 7


def minimum_value(value1, value2):
    minval = min(value1, value2)
    return minval


print(minimum_value(value1, value2))
