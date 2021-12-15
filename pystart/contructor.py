from typing import Type, Any, Callable

_T = Any


class A:
    def __new__(cls: Type[_T], a: Any) -> _T:
        print(f"this is __new__{a}\n")
        return object.__new__(cls)  # type: ignore
        # return cls.__init__(,a)
        # return cls(a)

    def __init__(self, a: int) -> None:
        print(f"this is __init__{a}")
        self.a = a


class demo(int):
    def __init__(self, arg: Any):
        self.arg = arg
        self.arg = round(self.arg, 4)
        print(self.arg)


class C:
    def __init__(self, c: Any) -> None:
        self.c = 0


class SubC(C):
    def __init__(self, b: Any) -> None:
        super().__init__(b)
        self.b = b


def f():
    return 1


def f1(fn: Callable[[int, int], int]):
    return fn(1, 1)


def f2(fn: Callable[..., Any]):
    ...


def f3(*agrs: Any):
    print("test *args")
    for item in agrs:
        print(item)


def f4(**kagrs: Any):
    print("test **kargs")
    for item in kagrs:
        print(item)


def f5(*agrs: Any, **kagrs: Any):
    for item in agrs:
        print("test *args")
        print(item)

    for item in kagrs:
        print("test **kargs")
        print(item)


def f6(p1: Any, p2: Any, p3: Any):
    print("unpack tuple")


if __name__ == "__main__":
    # a = A(3)
    # print(a.a)
    # print(type(a))
    # print(type(A))
    # a = demo(3.1415926)
    # print(a)

    # sub_c = SubC(1)
    # print(sub_c.c)
    # print(sub_c.b)
    # print(type(f))
    # def f_p(a: int, b: int) -> int:
    #     return a + b

    # class C_p:

    #     def __init__(self, a, b) -> None:
    #         print("init a instance of C_p")
    #         self.a = a
    #         self.b = b

    #     def __call__(self,a,b) -> Any:
    #         return a+b

    # cp = C_p(a=1, b=2)
    # print(f1(cp(1, 2)))
    # print(f1(f_p))

    t = {"x": 1, "y": 2, "z": 3}
    f4(**t)
    # f4(**t)

    # f3(t)
    # f3(*t)
    # f6(*t)

    # pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
    # pairs.sort(key=lambda pair: pair[0])
    # print(pairs)
