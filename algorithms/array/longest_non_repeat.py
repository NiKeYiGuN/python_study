"""
Given a string, find the length of the longest substring
without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""
import random
import string
from collections import defaultdict

from util.time_util import timer


@timer
def longest_non_repeat_v1(chars: str) -> int:
    """
    Violent method
    """
    max_sub_len = 0

    string_len = len(chars)
    for i in range(string_len):
        for j in range(string_len - i):
            if len(set(chars[i : i + j + 1])) != len(chars[i : i + j + 1]):
                continue
            max_sub_len = max(max_sub_len, len(chars[i: i + j + 1]))

    print("The longest substring length:", max_sub_len)
    return max_sub_len


@timer
def longest_non_repeat_v2(chars: str) -> int:
    max_sub_len = 0
    string_len = len(chars)

    for i in range(string_len):
        sub_len = 0
        sub_string = set()
        for j in range(i + 1, string_len):
            if chars[j] in sub_string or j == string_len - 1:
                sub_len = j - i-1
                break
            else:
                sub_string.add(chars[j])

        max_sub_len = max(sub_len, max_sub_len)

    print("The longest substring length:", max_sub_len)
    return max_sub_len


@timer
def longest_non_repeat_v3(chars: str) -> int:
    right, left = 0, 0
    times_map = defaultdict(int)
    max_sub_len = 0
    string_len = len(chars)

    for right in range(string_len):
        times_map[chars[right]] += 1
        while times_map[chars[right]] > 1:
            times_map[chars[left]] -= 1
            left += 1

        max_sub_len = max(max_sub_len, right - left + 1)

    print("The longest substring length:", max_sub_len)
    return max_sub_len


@timer
def longest_non_repeat_v4(chars: str) -> int:
    right, left = 0, 0
    index_map = {}
    max_sub_len = 0
    string_len = len(chars)

    for right in range(string_len):
        if chars[right] in index_map and index_map[chars[right]] >= left:
            left = index_map[chars[right]] + 1

        index_map[chars[right]] = right
        max_sub_len = max(max_sub_len, right - left + 1)

    print("The longest substring length:", max_sub_len)
    return max_sub_len


if __name__ == "__main__":
    letters = ""

    for i in range(2000):
        letters += random.choice(string.ascii_lowercase)

    longest_non_repeat_v1(letters)
    longest_non_repeat_v2(letters)
    longest_non_repeat_v3(letters)
    longest_non_repeat_v4(letters)
