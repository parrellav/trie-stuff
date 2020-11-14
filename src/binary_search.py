# assumes list is sorted
def find_value_in_sorted_list(lst, val):
    found, found_left, found_right = False, False, False
    mid_index = len(lst) // 2
    if 1 == len(lst):
        return val == lst[0]
    if val == lst[mid_index]:
        return True
    elif val < lst[mid_index]:
        found_left = find_value_in_sorted_list(lst[:mid_index], val)
    else:
        found_right = find_value_in_sorted_list(lst[mid_index:], val)
    return max(found, max(found_left, found_right))

def find_val(list, val):
    found_left, found_right, found = False, False, False
    if len(list) == 1:
        return val == list[0]
    middle_index = len(list) // 2
    if val == list[middle_index]:
        return True
    if val < list[middle_index]:
        found_left = find_val(list[:middle_index], val)
    else:
        found_right = find_val(list[middle_index:], val)
    return max(found_left, found_right)