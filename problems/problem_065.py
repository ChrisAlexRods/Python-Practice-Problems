# Write a function that meets these requirements.
#
# Name:       biggest_gap
# Parameters: a list of numbers that has at least
#             two numbers in it
# Returns:    the largest gap between any two
#             consecutive numbers in the list
#             (this will always be a positive number)
#
# Examples:
#     * input:  [1, 3, 5, 7]
#       result: 2 because they all have the same gap
#     * input:  [1, 11, 9, 20, 0]
#       result: 20 because from 20 to 0 is the biggest gap
#     * input:  [1, 3, 100, 103, 106]
#       result: 97 because from 3 to 100 is the biggest gap
#
# You may want to look at the built-in "abs" function
numbers = [1, 11, 9, 20, 0]
#don't entirely understand waht's happening. Espicially the logic
def biggest_gap(nums):
    max_gap = 0
    #this is making it so the second number is subtracted from the first number. abs is making sure if the result is negattive
    #then it is return as the "true value": the positive version of that number
    for i in range(len(nums) - 1):
        gap = abs(nums[i + 1] - nums[i])
        if gap > max_gap:
            max_gap = gap
    return max_gap

print(biggest_gap(numbers))