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