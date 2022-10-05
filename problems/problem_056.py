# Write a function that meets these requirements.
#
# Name:       num_concat
# Parameters: two numerical parameters
# Returns:    the concatenated string conversions
#             of the numerical parameters
#
# Examples:
#     input:
#       parameter 1: 3
#       parameter 2: 10
#     returns: "310"
#     input:
#       parameter 1: 9238
#       parameter 2: 0
#     returns: "92380"
num1= 100
num2 = 200
def num_concat(num1,num2):
    # concatenated just means adding the strings. Because we're taking integars
    #we have to convert them intro strings inside the return function
    return str(num1) + str(num2)


print(num_concat(num1,num2))
