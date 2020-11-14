import math
import copy
from collections import deque
from heapq import *

def findMaxLenSubSeq(arr):
    arr_as_set = set(arr)
    seq_length = 0
    for a in arr_as_set:

        # are we in a sequence already
        if a-1 not in arr_as_set:
            inc = 1
            while a+inc in arr_as_set:
                inc += 1

        if seq_length < inc:
            seq_length = inc
    return seq_length

# Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
# minimumBribes has the following parameter(s):
# q: an array of integers

def minimumBribes(q):
    TOO_CHAOTIC = 'Too chaotic'
    swaps = 0
    length = len(q)
    i = 0
    while i < length:
        current_val = q[i]
        look_ahead = i + 1
        if current_val != look_ahead and look_ahead < length:
            offset = abs(current_val - q[look_ahead])
            if offset > 2:
                return TOO_CHAOTIC
            else:
                swaps += offset
                i += offset + 1
    return swaps


def find_max_sum_subarray(size, array):
    max_sum = 0
    sum = 0
    elements = [None] * size
    for i in range(len(array)):
        sum += array[i]
        if i > size-1:
            sum -= array[i-size]
        if sum > max_sum:
            max_sum = sum
    return max_sum


def smallest_subarray_greater_than_or_equal_to_given_sum(sum, array):
    size = len(array)
    _sum = 0
    for i in range(len(array)):
        if array[i] >= sum:
            return 1
        _sum += array[i]
        if _sum >= sum:
            size = i + 1

    return size

def _fruits_recur(fruit):
    fruits_collected = 0
    length = len(fruit)
    if length == 0:
        return fruits_collected
    my_dict = {}
    for i in range(length):
        current_fruit = fruit[i]
        if current_fruit not in my_dict and len(my_dict) >= 2:
            break
        if current_fruit not in my_dict:
            my_dict[current_fruit] = 0
        my_dict[current_fruit] += 1
    fruits_collected = sum(my_dict.values())
    return max(fruits_collected, _fruits_recur(fruit[1:]))


def fruits_into_baskets(fruit):
    return _fruits_recur(fruit)

def pair_with_targetsum(arr, target_sum):
    length = len(arr)
    left_ptr = 0
    right_ptr = length - 1
    while left_ptr != right_ptr:
        sum = arr[left_ptr] + arr[right_ptr]
        if sum == target_sum:
            return [left_ptr, right_ptr]
        if sum > target_sum:
            right_ptr -= 1
        else:
            left_ptr += 1
    return [-1, -1]

def make_squares(arr):
    squares = []
    for i in arr:
        temp = i * i
        squares.append(temp)
        j = 0
        end = len(squares) - 1
        while end > 0:
            if squares[end] < squares[end - 1]:
                squares[end], squares[end-1] = squares[end-1], squares[end]
            end -= 1
    return squares


def shortest_window_sort(arr):
    length = len(arr)
    left, right = 0, length - 1
    left_bound = 0
    right_bound = right
    while left < length and right > 0:
        if arr[left] > arr[left + 1]:
            left_bound = left + 1
        left += 1
        if arr[right] < arr[right - 1]:
            right_bound = right - 1
        right -= 1
    return right_bound - left_bound


def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    print('hi')
    return -1


def find_subsets(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        clones = copy.deepcopy(subsets)
        for clone in clones:
            clone.append(num)
            subsets.append(clone)
    return subsets


def find_permutations(nums):
    num_length = len(nums)
    result = []
    perms = deque()
    perms.append([])
    for num in nums:
        n = len(perms)
        for _ in range(n):
            oldperm = list(perms.popleft())
            for i in range(len(oldperm) + 1):
                newPerm = list(oldperm)
                newPerm.insert(i, num)
                if len(newPerm) == num_length:
                    result.append(newPerm)
                else:
                    perms.append(newPerm)
    return result

def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    for chr in str:
        if chr.isalpha():
            perm_length = len(permutations)
            for i in range(perm_length):
                newPerm = list(permutations[i])
                j = 0
                while newPerm[j] is not chr:
                    j +=1
                newPerm[j] = newPerm[j].swapcase()
                permutations.append(''.join(newPerm))


    return permutations

def find_Kth_smallest(lists, k):
    minHeap = []

    for i in range(len(lists)):
        tuple = (lists[i][0], 0, lists[i])
        heappush(minHeap, tuple)

    # take the smallest(top) element form the min heap, if the running count is equal to k return the number
    numberCount, number = 0, 0
    while minHeap:
        number, i, list = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            break
        # if the array of the top element has more elements, add the next element to the heap
        if len(list) > i+1:
            heappush(minHeap, (list[i+1], i+1, list))

    return number
