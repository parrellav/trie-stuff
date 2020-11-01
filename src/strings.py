
def repeatedString(s, n):
    s_length = len(s)
    full_times = n // s_length
    partial_chars = n % s_length
    remainder = s[0:partial_chars]
    counts_in_partial = 0
    a_indexes = []
    for i in range(s_length):
        if 'a' == s[i]:
            a_indexes.append(i)
            if i < partial_chars:
                counts_in_partial += 1

    repeated_char_in_base_string = len(a_indexes)
    return repeated_char_in_base_string * full_times + counts_in_partial

### does not work well
def longest_common_substring(s1, s2):
    longest_common = 0
    current = 0
    j = 0
    for i in range(len(s2)):
        if j < len(s1):
            while s2[i] != s1[j]:
                if j == len(s1) - 1:
                    break
                j += 1
            longest_common += 1
            j += 1

    return longest_common - 1

### from educative
def longest_common_substr_length(s1, s2):
    """
    Finds a longest common substring length
    :param s1: First string
    :param s2: Second string
    :return: Length of longest common substring
    """

    # Initializing all values in lookup_table to zero
    lookup_table = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

    max_length = 0
    for i in range(len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                lookup_table[i][j] = 1 + lookup_table[i - 1][j - 1]
                max_length = max(max_length, lookup_table[i][j])

    return max_length


def _shortest_substring(str, alpha_dict):
    length = len(str)
    for i in range(length):
        if str[i] in alpha_dict:
            alpha_dict[str[i]] = alpha_dict[str[i]] + 1

    if 3 == sum(alpha_dict.values()):
        return str
    return _shortest_substring(str[1:], alpha_dict.fromkeys(alpha_dict, 0))


def shortest_substring_in_alphabet(str, alphabet):
    alpha_dict = {letter: 0 for letter in alphabet}
    return _shortest_substring(str, alpha_dict)


def longest_substring_with_no_more_than_k_characters(str, k):
    char_counts = {}
    start_position = 0
    max_str_length = 0
    for i in range(len(str)):
        current = str[i]
        # result += current
        if current not in char_counts:
            char_counts[current] = 0
        char_counts[current] += 1
        while len(char_counts) > k:
            to_remove = str[start_position]
            char_counts[to_remove] -= 1
            if char_counts[to_remove] == 0:
                char_counts.pop(to_remove, None)
            start_position += 1
        max_str_length = max(max_str_length, i-start_position + 1)
    return max_str_length


def _non_repeat_substring_recur(str):
    longest = 0
    length = len(str)
    if length == 0:
        return longest
    my_dict = set()
    for i in range(length):
        current = str[i]
        if current in my_dict:
            break
        my_dict.add(current)
        longest += 1
    return max(longest, _non_repeat_substring_recur(str[1:]))

def find_longest_substring_without_repeats(str):
    return _non_repeat_substring_recur(str)


def backspace_compare(str1, str2):
    # Two pointer approach
    new_s1, new_s2 = '', ''
    str1_left = 0
    str2_left = 0
    while str1_left < len(str1) and str2_left < len(str2):
        if str1[str1_left] == '#':
            new_s1 = new_s1[:-1]
        else:
            new_s1 += str1[str1_left]
        str1_left += 1
        if str2[str2_left] == '#':
            new_s2 = new_s2[:-1]
        else:
            new_s2 += str2[str2_left]
        str2_left += 1

    return new_s1 == new_s2