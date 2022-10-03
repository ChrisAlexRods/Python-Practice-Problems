# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if (x and y) >= 0 and (x and y) < 11:
        return "inclusive"
    else:
        return "not inclusive"

print(is_inside_bounds(0,10))
print(is_inside_bounds(30,29))
