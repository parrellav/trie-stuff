import random


def choose_pivot(lst, left, right):
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    return max(min(i1, i2), min(max(i1, i2), i3))


def partition(lst, left, right):
    pivot_index = choose_pivot(lst, left, right)

    lst[right], lst[pivot_index] = lst[pivot_index], lst[right]
    pivot = lst[right]
    i = left - 1

    for j in range(left, right):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[right] = lst[right], lst[i+1]
    return i + 1


def quick_sort(lst, left, right):
    if left < right:
        pi = partition(lst, left, right)

        quick_sort(lst, left, pi - 1)
        quick_sort(lst, pi + 1, right)