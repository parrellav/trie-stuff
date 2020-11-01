# list only has zeros, ones and twos
# find a zero? put it at the beginning
# find a one, leave it
# find a two, put it at the end
def sort_list_of_zero_one_two(lst):
    i = 0
    mid = 0
    end = len(lst) - 1
    while mid < end:
        if lst[mid] == 0:
            lst[i], lst[mid] = lst[mid], lst[i]
            mid += 1
            i += 1
        elif lst[mid] == 2:
            lst[mid], lst[end] = lst[end], lst[mid]
            end -= 1
        else: # we must be looking at a 1
            mid += 1
    return lst