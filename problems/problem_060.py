# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
#     * input:   [1, 2, 3, 4]
#       returns: [1, 3]
#     * input:   [2, 4, 6, 8]
#       returns: []
#     * input:   [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]
def only_odds(numbers):
    odd_numbers = []
# we need the an empty lsit because we need to
    for number in numbers:
        # the plural
        if number % 2 == 1:
            # the math being 2 is smashed into the number until the remainder is lst. If it's 1 it's an odd number
            odd_numbers.append(number)
            # append the
    return odd_numbers
numbers = [1, 2, 3, 4]
print(only_odds(numbers))
