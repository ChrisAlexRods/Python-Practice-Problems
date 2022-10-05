# Complete the translate function which accepts two
# parameters, a list of keys and a dictionary. It returns a
# new list that contains the values of the corresponding
# keys in the dictionary. If the key does not exist, then
# the list should contain a None for that key.
#
# Examples:
#   * keys:       ["name", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     ["Noor", 29]
#   * keys:       ["eye color", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [None, 29]
#   * keys:       ["age", "age", "age"]
#     dictionary: {"name": "Noor", "age": 29}
#     result:     [29, 29, 29]
#
# Remember that a dictionary has the ".get" method on it.

key_list = ["name", "age", "dog"]
dictionary = {"name": "Noor", "age": 29}

def translate(key_list, dictionary):
    result = []
    for key in key_list:
        if key in dictionary:
            get_value = dictionary.get(key)
            result.append(get_value)
        else:
            result.append(None)
    return result

print(translate(key_list, dictionary))
