# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.
x = 7
y = 6


def is_inside_bounds(x, y):
    if x in range(0, 10):
        return True
    if y in range(0, 10):
        return True
    else:
        return False
