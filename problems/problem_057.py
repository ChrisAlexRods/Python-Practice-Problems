# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4

#i missread the question
def sum_fraction_swquence(numbers):
    #beacuse we're looking for the sum we need to have a variable equal to zero that will hold the final value
    sum = 0
    for number in range(1 , numbers + 1):
        #number is a place holder for numbers. in range is establishing that the number we input will be the limiter for the loop.
        # if i put a input of 2 the range would be (1,3). in out case its (1, 4)
        sum = sum + number/(number + 1)
        #sum is varaible we're going to return to. sum + (number/(number+1)) the previo sum is getting added to the new one
        #until we reach the range
    return sum

print(sum_fraction_swquence(3))
