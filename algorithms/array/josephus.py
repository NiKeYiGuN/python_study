"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""
import copy
from typing import List, Any


def josephus(array: List[float]) -> List[float]:
    skip = 1
    p = 0
    res = []

    while array:
        if len(array) < 3:
            res.extend(array[::-1])
            array.clear()

        if skip % 3 == 0:
            res.append(array.pop(p))
        else:
            p += 1

        if p == len(array):
            p = 0

        skip += 1

    return res


def josephus_yield(array: List[float]) -> Any:
    skip = 2
    idx = 0
    array_length = len(array)

    while array_length:
        idx = (idx + skip) % array_length  # 通过取余的方法来获取需要挑出来的数字
        yield array.pop(idx)
        array_length -= 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr1 = copy.copy(arr)
    print(list(josephus_yield(arr)))
    print(josephus(arr1))
