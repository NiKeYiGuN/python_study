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
from util.time_util import timer


@timer
def longest_non_repeat_v1(string: str) -> None:
    """
    Violent method
    """
    max_sub_len = 0

    string_len = len(string)
    for i in range(string_len):
        for j in range(string_len - i):
            if len(set(string[i : i + j + 1])) != len(string[i : i + j + 1]):
                continue
            max_sub_len = max(max_sub_len, len(string[i : i + j + 1]))

    print("The longest substring length:", max_sub_len)


@timer
def longest_non_repeat_v2(string: str) -> None:
    max_sub_len = 0

    string_len = len(string)
    for i in range(string_len):
        sub_len = 0
        sub_string = set()
        for j in range(i, string_len):
            if string[j] in sub_string:
                sub_len = j - i
                break
            else:
                sub_string.add(string[j])

        max_sub_len = max(sub_len, max_sub_len)

    print("The longest substring length:", max_sub_len)


if __name__ == "__main__":
    longest_non_repeat_v1("abcabcb")
    longest_non_repeat_v2("abcabcbb")