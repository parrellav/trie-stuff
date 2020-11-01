# doesn't work
def _find_nth_fib(n, lookup):
    if n < 2:
        return n

    if lookup[n] is None:
        lookup[n] = _find_nth_fib(n-1, lookup) + _find_nth_fib(n-2, lookup)
    return lookup[n]


def find_nth_fib(n):
    lookup = [None] * (n + 1)

    return _find_nth_fib(n, lookup)

def fib_map(num):
    if num == 0:
        raise Exception('Index must be greater than zero')

    lookup = {1: 0, 2: 1}

    if num not in lookup:
        for x in range(3, num+1):
            lookup[x] = lookup[x-1] + lookup[x-2]

    return lookup[num]