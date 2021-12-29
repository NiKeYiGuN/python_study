from algorithms.array.flatten import flatten, flatten_iter


def test_flatten():
    assert flatten([1, 1, 1, ["a", "b", "c"]], []) == [1, 1, 1, "a", "b", "c"]


def test_flatten_iter():
    assert list(flatten_iter([1, 1, 1, ["a", "b", "c"]])) == [1, 1, 1, "a", "b", "c"]
