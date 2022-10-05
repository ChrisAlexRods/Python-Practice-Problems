# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem
word = "abcdef"
def shift_letter(word):
    #we're using an empty string because the RETURN SAYS STRING
    lst = ""
    # we are looking to loop the problem
    for letter in word:
        #abocve we stated certain conditions if the letter was capitol
        if letter == "Z":
            new_letter = "A"
        if letter == "z":
            new_letter = "a"
            #if they're not any of the letter above then we get to the actual function in the else statement
        else:
            #ord = the computer code. a integer that can be changed.the chr is retruning it back as letter. the + 1 is added after the ord converts the letter into a number
            new_letter = chr(ord(letter) + 1)
            #becuase it's being added to a string we can just add each new letter intoa empt string
            lst = lst + new_letter
    return lst

print(shift_letter(word))
