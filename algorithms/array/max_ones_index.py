"""
Find the index of 0 to be replaced with 1 to get
the longest continuous sequence
of 1s in a binary array.
Returns index of 0 to be
replaced with 1 to get the longest
continuous sequence of 1s.
If there is no 0 in array, then
it returns -1.
e.g.
let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
If we replace 0 at index 3 with 1, we get the longest continuous
sequence of 1s in the array.
So the function return => 3
"""
from util.time_util import timer


@timer
def get_max_ones_index(arr: list[int]) -> int:
    arr_len = len(arr)
    max_count = 0
    max_index = 0
    pre = -1
    pre_pre = -1

    for i in range(arr_len):
        if arr[i] == 0:
            pre_pre = pre
            pre = i

        if max_count >= i - pre_pre:
            max_index = pre_pre
        else:
            max_index = pre

        max_count = max(max_count, i - pre_pre)

    print("max_count:", max_count)
    return max_index


if __name__ == "__main__":
    import numpy as np

    test_array = np.random.randint(0, 2, 100)
    print(get_max_ones_index(test_array))

