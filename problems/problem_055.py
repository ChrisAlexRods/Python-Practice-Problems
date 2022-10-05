# Write a function that meets these requirements.
#
# Name:       simple_roman
# Parameters: one parameter that has a value from 1
#             to 10, inclusive
# Returns:    the Roman numeral equivalent of the
#             parameter value
#
# All examples
#     * input: 1
#       returns: "I"
#     * input: 2
#       returns: "II"
#     * input: 3
#       returns: "III"
#     * input: 4
#       returns: "IV"
#     * input: 5
#       returns: "V"
#     * input: 6
#       returns: "VI"
#     * input: 7
#       returns: "VII"
#     * input: 8
#       returns: "VIII"
#     * input: 9
#       returns: "IX"
#     * input: 10
#       returns:  "X"
def simple_roman(value):
    #This is suppsoed to be a dictionary question. When a user input a number you use a dictionary
    #to idetify the key, then pull the nubmer out
    roman_dictionary = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "IV",
        6: "V",
        7: "VI",
        8: "VIII",
        9: "IX",
        10: "X"
    }
    return roman_dictionary[value]
#When you return the dictionary you need the [] to specifiy what you want the input to be for the dictioanry
# if you don't the print statement prints the entire dictionary.
#
print(simple_roman(4))
