# type: ignore
from operator import le
from re import A
from typing import Generic, Iterable, TypeVar


T = TypeVar("T")


class Mylist(list, Generic[T]):
    def __init__(self, content: Iterable[T]):
        super().__init__(content)

    def sort(self):
        for k in range(1, len(self)):
            cur = self[k]
            j = k
            while j > 0 and self[j - 1] > cur:
                self[j] = self[j - 1]
                j -= 1
                self[j] = cur

        return self

    def bubble_sort(self):
        for i in range(1, len(self)):
            for j in range(len(self) - i):
                if self[j] > self[j + 1]:
                    self[j], self[j + 1] = self[j + 1], self[j]

        return self
    

    def selection_sort(self):
        for i in range(len(self) - 1):
            minIndex = i
            for j in range(i + 1, len(self)):
                if self[j] < self[minIndex]:
                    minIndex = j
            # i 不是最小数时，将 i 和最小数进行交换
            if i != minIndex:
                self[i], self[minIndex] = self[minIndex], self[i]
        return self


if __name__ == "__main__":
    mylist = Mylist([6, 2, 3, 4, 5])
    assert mylist.sort() == [2, 3, 4, 5, 6]
    assert mylist.bubble_sort() == [2, 3, 4, 5, 6]
