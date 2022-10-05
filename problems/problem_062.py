# Write a function that meets these requirements.
#
# Name:       basic_calculator
# Parameters: left, the left number
#             op, the math operation to perform
#             right, the right number
# Returns:    the result of the math operation
#             between left and right
#
# The op parameter can be one of four values:
#   * "+" for addition
#   * "-" for subtraction
#   * "*" for multiplication
#   * "/" for division
#
# Examples:
#     * inputs:  10, "+", 12
#       result:  22
#     * inputs:  10, "-", 12
#       result:  -2
#     * inputs:  10, "*", 12
#       result:  120
#     * inputs:  10, "/", 12
#       result:  0.8333333333333334
#before we even start. You need to get better at evualiting the parameters and understanding the question before starting
# almost made a super complicated calcualter
def basic_calculater(left, op, right):
    #becuase we're given three parameters. One of which being the oeprator. We can isoalte it and change our code around it
    # Becuasse we're not looping, we  can identify the 4 possible operators and make the op == string
    #so if we repeat the process
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if op == "/":
        return left / right

print(basic_calculater(10 , "+", 5))
print(basic_calculater(10 , "-", 5))
print(basic_calculater(10 , "*", 5))
print(basic_calculater(10 , "/", 5))