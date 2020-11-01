def find_sum(lst: list, n: int):
    results = []
    for i in lst:
        desired = n - i
        if desired in lst:
            results.append(i)
            results.append(desired)
            break
    return results


def find_element_in_list_i_cheated(lst, n, key):
    big_dict = {}
    for elem in lst:
        big_dict[elem] = lst.index(elem)
    return big_dict[key]


def pivoted_binary_search(lst, n, key):
    """
    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """
    if n > 1:
        half = n // 2  # round the result

        right_half = lst[half:]
        left_half = lst[:half]

        pivoted_binary_search(right_half, len(right_half), key)
        pivoted_binary_search(left_half, len(left_half), key)

# not complete
def sort_binary_list(lst):
    length = len(lst)
    mid = length // 2

    if length == 2:
        if lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
        return lst

    if length > 1:
        left_res = sort_binary_list(lst[:mid])
        right_res = sort_binary_list(lst[mid:])
        return left_res + right_res

def find_max_prod(lst):
    lst = sorted(lst)
    max_prod = 0
    max_prod_pair = []
    lst_length = len(lst)
    for i in range(lst_length):
        j = i + 1
        if j != lst_length:
            prod = lst[i] * lst[j]
            if prod > max_prod:
                max_prod_pair = [lst[i], lst[j]]
    return max_prod_pair[0], max_prod_pair[1]

def search_two_d_list(matrix, num_to_find):
    found = False
    for row in matrix:
        length = len(row)
        if row[length - 1] > num_to_find:
            for i in range(length-1, 0, -1):
                if row[i] == num_to_find:
                    found = True
                    break
    return found

def search_insert_position(lst, value):
    """
    A function to search insert position of a given value in a list
    :param lst:  A list of integers
    :param value: An integer
    :return: The position of the value to be in the list
    """

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    print('hi')