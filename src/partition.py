def can_partition(set):
    """
    Checks if two sub-lists has equal sum or not
    :param set: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """
    lookup = {}
    my_list = list(set)
    # Write your code here!
    result = False
    length = len(set)
    for i in range(length - 1):
        j = i + 1
        while j < length:
            sum = my_list[i] + my_list[j]
            if sum in lookup:
                result = True
            else:
                lookup[sum] = ((my_list[i], my_list[j]))
            j += 1

    return result