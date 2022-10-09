# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one
import random

def specific_random():
    #using this to establish the range to the varible. You can also add the range to Nubmers in the for statemnet.
    numbers = range(10, 500)
    #because we're looking for a single number within the range we need an empty list to append too
    lst = []

    for number in numbers:
        if number % 5 == 0 and number % 7 == 0:
            # you can have 2 statements if true as long as the : is gone and you only need to use one if statement.
            lst.append(number)
            #we're appending thne number that satisfies the if statement
    return random.choice(lst)
#This one was funky. you had to look at all the viable random functions on pydocs you could import
print(specific_random())
