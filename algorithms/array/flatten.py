"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
e.g.:[1, 2, 3, [1, 2, 3]]=>[1, 2, 3, 1, 2, 3]
"""
from typing import List, Any, Iterator
from collections.abc import Iterable


# return list
def flatten(input_arr: List[Any], output_arr: List[Any]) -> List[Any]:
    if output_arr is None:
        output_arr = []

    for item in input_arr:
        if isinstance(item, Iterable) and not isinstance(item, str):
            flatten(item, output_arr)
        else:
            output_arr.append(item)

    return output_arr


def flatten_iter(input_arr: List[Any]) -> Iterator:
    for item in input_arr:
        if isinstance(item, Iterable) and not isinstance(item, str):
            yield from flatten_iter(item)
        else:
            yield item


if __name__ == "__main__":
    array = [1, 2, 3, [1, 2, 3]]
    output = []

    print(flatten(input_arr=array, output_arr=output))
    print(list(flatten_iter(array)))
