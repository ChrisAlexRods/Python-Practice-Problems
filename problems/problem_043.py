# Complete the find_indexes function which accepts two
# parameters, a list and a search term. It returns a new
# list that contains the indexes of the search term in
# the search list.
#
# Remember that indexes in Python are zero-based. That
# means the first element in the list is index 0.
#
# Examples:
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  4
#     result:       [3]
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  6
#     result:       []
#   * search_list:  [1, 2, 1, 2, 1]
#     search_term:  1
#     result:       [0, 2, 4]
#
# Look up the enumerate function to help you with this problem.
search_list = [1, 2, 3, 4, 5]
search_term = 100

def find_indexes(search_list, search_term):
    if search_term in search_list:
        return True
    else:
        return False
    
    # """
    # result = 0
    # for value1 in (search_list):
    #     if value1 ==  search_term:
    #         result.append(value1)
    # return result
    # """
print(find_indexes(search_list,search_term))
