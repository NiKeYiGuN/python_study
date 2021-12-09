from data_strucures.sorted import Mylist


def test_list_sorted():
    mylist = Mylist([6, 2, 3, 4, 5])

    assert mylist.sort() == [2, 3, 4, 5, 6]
    assert mylist.bubble_sort() == [2, 3, 4, 5, 6]
