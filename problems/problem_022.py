# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"
is_workday = True
is_sunny = True


def gear_for_day(is_workday, is_sunny):

    lst = []
    if is_workday and is_sunny:
        lst.append("Umbrella")
    if is_workday:
        lst.append("Laptop")
    if not is_workday:
        lst.append("surfboard")
    return lst


print(gear_for_day(is_workday, is_sunny))