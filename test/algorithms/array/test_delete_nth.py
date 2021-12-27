from algorithms.array.delete_nth import delete_nth_native, delete_nth


def test_delete_nth_navite():
    assert delete_nth_native([1, 1, 1], 1) == [1]


def test_delete_nth():
    assert delete_nth([1, 2, 3], 1) == [1, 2, 3]
