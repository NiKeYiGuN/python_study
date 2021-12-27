"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3]
"""
from collections import defaultdict
from typing import List


# time compex o(n^2)
def delete_nth_native(array: List[int], n: int) -> List[int]:
    result = []
    for item in array:
        if result.count(item) < n:
            result.append(item)

    return result


# time complexity o(n),using hash table
def delete_nth(array: List[int], n: int) -> List[int]:
    counts = defaultdict(int)
    for item in array:
        if counts[item] < n:
            counts[item] += 1

    return list(counts.keys())


if __name__ == "__main__":
    print(delete_nth_native([1, 2, 3, 1, 2, 1, 2, 3], 2))
    print(delete_nth_native([1, 2, 3, 1, 2, 1, 2, 3], 2))
