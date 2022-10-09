# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.
attendees_list = ["bob", "tim"]
members_list = ["geg", "fgafs", "asfsf"]


def has_quorum(attendees_list, members_list):
    attend = len(attendees_list)
    member = len(members_list)

    if attend / member >= .5:
        return True
    else:
        return False


print(has_quorum(attendees_list, members_list))