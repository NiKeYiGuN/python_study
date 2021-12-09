from dataclasses import dataclass, field
from typing import List


@dataclass(repr=True, eq=True, frozen=True)
class A:
    l: List[float] = field(default_factory=list, hash=False)
    x: float = 4
    X: int = 5

    def add(self):
        return self.X + self.x

    # def __setattr__(self, name: str, value: Any):
    #     self.__dict__[name] = value
    #     return self


class BB:
    # def __init__(self, a) -> None:
    #     self.a = a
    ...


if __name__ == "__main__":
    # a = A()
    # print(a.__hash__())
    # -1009709641759730766
    # print(fields(A))
    # a.x = 6
    # print(a.x)
    # print(A.__dict__["__init__"])
    # print(B.__dict__)

    # print(a.__dict__)
    # print(a.x)
    # print(A.x)
    # print(A.X)
    # print(a.X)
    # print(A)
    # print(fields(a))
    # print(int())
    # A.x = 6
    # print(A.x)
    class B:
        X = 1

    # print(getattr(B, "X", None))  # type: ignore
    print(ascii(B()))
    print(bytearray("abc", encoding="utf-8"))
    # print("\040")
    exec("x=1+1")
    print(x)  # type: ignore
    assert x == 2  # type: ignore
