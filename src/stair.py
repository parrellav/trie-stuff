# counts the ways a person can ascend n stairs using 1, 2 or 3 steps at a time
def count_ways_recurse(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return count_ways_recurse(n-1) + count_ways_recurse(n-2) + count_ways_recurse(n-3)

# this doesn't work for some reason, it returns a value too low
def count_steps_memoiz(n):
    res = [0]*(n + 2)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1):
        res[i] = res[n-1] + res[n-2] + res[n-3]

    return res[n]