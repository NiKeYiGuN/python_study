from typing import List


class Lib(object):
    def __init__(self, curr: float, prev: float):
        self.prev: float = prev
        self.curr: float = curr

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


class Acc(object):
    def __init__(self):
        self.a = 1

    def __iter__(self):
        print("__iter__ from Acc")
        return self

    def __next__(self):
        print("__next__ from Acc")
        self.a = self.a + 1
        if self.a > 10:
            raise StopIteration()
        return self.a

    def my_next(self):
        return self.a + 1000


class Fib(object):
    def __init__(self, m: float):
        self.a, self.b = 0, 1
        self.m = m
        self.A = Acc()

    def __iter__(self):
        print("__iter__ form Fib")
        if self.m == 5:
            return self.A
        else:
            return self

    def __next__(self):
        print("__next__ from Fib")
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def my_next(self):
        return self.a + 1


def isValidSudoku(board: List[List[str]]) -> bool:
    for row in board:
        temp = []
        for num in row:
            if num in temp:
                return False
            elif num != ".":
                temp.append(num)  # type: ignore

    for i in range(9):
        temp1 = []
        for j in range(9):
            if board[j][i] in temp1:
                return False
            elif board[j][i] != ".":
                temp1.append(board[j][i])  # type: ignore
    for n in range(3):
        for m in range(3):
            if n == 0 and m == 2:
                print("n==0,m==2")
            for i in range(3):
                temp2 = []
                for j in range(3):
                    if board[n * 3 + i][m * 3 + j] in temp2:
                        return False
                    elif board[n * 3 + i][m * 3 + j] != ".":
                        temp2.append(board[n * 3 + i][m * 3 + j])  # type: ignore

    return True


if __name__ == "__main__":
    # f = Lib(0, 1)
    # print(list(islice(f, 0, 20)))
    # f = [
    #     [".", ".", ".", ".", "5", ".", ".", "1", "."],
    #     [".", "4", ".", "3", ".", ".", ".", ".", "."],
    #     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    #     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    #     [".", ".", "2", ".", "7", ".", ".", ".", "."],
    #     [".", "1", "5", ".", ".", ".", ".", ".", "."],
    #     [".", ".", ".", ".", ".", "2", ".", ".", "."],
    #     [".", "2", ".", "9", ".", ".", ".", ".", "."],
    #     [".", ".", "4", ".", ".", ".", ".", ".", "."],
    # ]
    #
    #
    #
    #
    # isValidSudoku(f)

    # x = Fib(5)
    # print("__next__方法输出")
    # print(x.__next__())
    # print(x.__next__())
    # print(x.__next__())
    # print(x.__next__())
    # print(x.__next__())
    #
    # print("mynext()方法输出")
    # print(x.my_next())
    # print(x.my_next())
    # print(x.my_next())
    # print(x.my_next())
    #
    # print("for in Fib(5)")
    # for n in Fib(5):  # for关键字调用了Fib类的__iter__方法
    #     print(n)
    #
    # m = Fib(5)
    # x = iter(m)
    # print(m.my_next())
    # print(x.__next__())
    # for n in x:
    #     print(n)
    #
    # print("再运行一次for循环：")
    # for n in iter(m):
    #     print(n)
    # print(m.my_next())

    s = "rat"
    t = "cat"
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list == t_list:
        print("1111")
