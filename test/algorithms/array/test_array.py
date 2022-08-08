import random
import string

from algorithms.array.delete_nth import delete_nth_native, delete_nth
from algorithms.array.flatten import flatten, flatten_iter
from algorithms.array.josephus import josephus, josephus_yield
from algorithms.array.longest_non_repeat import longest_non_repeat_v1, longest_non_repeat_v2, longest_non_repeat_v3, \
    longest_non_repeat_v4
from algorithms.array.max_ones_index import get_max_ones_index


def test_delete_nth_navite():
    assert delete_nth_native([1, 1, 1], 1) == [1]


def test_delete_nth():
    assert delete_nth([1, 2, 3], 1) == [1, 2, 3]


def test_flatten():
    assert flatten([1, 1, 1, ["a", "b", "c"]], []) == [1, 1, 1, "a", "b", "c"]


def test_flatten_iter():
    assert list(flatten_iter([1, 1, 1, ["a", "b", "c"]])) == [1, 1, 1, "a", "b", "c"]


def test_garage():
    ...  # TODO: Need test print() function.


def test_josephus():
    assert josephus([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [3, 6, 9, 4, 8, 5, 2, 7, 1]


def test_josephus_yield():
    assert list(josephus_yield([1, 2, 3, 4, 5, 6, 7, 8, 9])) == [3, 6, 9, 4, 8, 5, 2, 7, 1]


def test_longest_non_repeat():
    chars = ""

    for i in range(1000):
        chars += random.choice(string.ascii_lowercase)

    assert longest_non_repeat_v1(chars) == longest_non_repeat_v2(chars)
    assert longest_non_repeat_v3(chars) == longest_non_repeat_v4(chars)


def test_max_ones_index():
    test_array = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    assert get_max_ones_index(test_array) == 9
