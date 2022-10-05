# Write a function that meets these requirements.
#
# Name:       temperature_differences
# Parameters: highs: a list of daily high temperatures
#             lows: a list of daily low temperatures
# Returns:    a new list containing the difference
#             between each high and low temperature
#
# The two lists will be the same length
#
# Example:
#     * inputs:  highs: [80, 81, 75, 80]
#                lows:  [72, 78, 70, 70]
#       result:         [ 8,  3,  5, 10]
highs = [80, 81, 75, 80]
lows = [72, 78, 70, 70]


def temperature_differences(highs, lows):
    #we're expecting a list back so make an empty function for that list
    lst = []
    #this is where i got confused
    #Becuase we want to combine two lists. we have to used the plural of both paramaeters
    #we're also going to used the zip function to combine the two list into an object:
    #once those two lists are combined we can append the mepty list with the subtraction of both lsits
    for high, low in zip(highs, lows):
        lst.append(high - low)
    return lst


print(temperature_differences(highs, lows))