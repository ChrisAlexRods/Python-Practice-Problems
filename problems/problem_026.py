# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average
values = [40, 90, 50]


def calculate_grade(values):
    lst = 0
    sum_values = sum(values)
    lst = sum_values / len(values)

    if lst >= 90:
        return "A"
    elif lst >= 80:
        return "B"
    elif lst >= 70:
        return "C"
    elif lst >= 60:
        return "D"
    elif lst >= 50:
        return "F"


print(calculate_grade(values))