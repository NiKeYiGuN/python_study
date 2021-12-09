# type: ignore

from typing import List


def binary_search(target: float, data: List[float]):
    low: int = 0
    high: int = len(data) - 1

    if low > high:
        return False
    mid: int = (low + high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(target, data[:mid])
    else:
        return binary_search(target, data[mid:])


if __name__ == "__main__":
    test_data = [1.0, 2, 3, 4, 5, 6, 7, 8]
    target = 1
    print(binary_search(target, test_data))
