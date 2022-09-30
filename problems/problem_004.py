# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def max_of_three(value1, value2, value3):
    if (value1 >= value2) or (value1 >= value3):
        # false                    false
        return value1
    if (value2 >= value1) or (value2 >= value3):
        # true                # true
        return value2
    if (value3 >= value1) or (value3 >= value2):
        return value3

print(max_of_three(1, 8, 3))