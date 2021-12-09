from dataclasses import (
    FrozenInstanceError,
    asdict,
    dataclass,
    field,
    astuple,
    is_dataclass,
    replace,
)
from typing import Any, List, ClassVar


@dataclass()
class B:
    l: List[float] = field(default_factory=list)
    x: float = 4
    X: int = 5

    def add(self):
        return self.X + self.x

    def __setattr__(self, name: str, value: Any):  # type: ignore
        self.__dict__[name] = value
        return self


class TestDataclass:
    def test_init(self):
        @dataclass(init=True)
        class C1:
            x: float = 1

        @dataclass(init=False)
        class C2:
            x: float = 1

        class C3:
            x: float = 1

        assert "__init__" in C1.__dict__
        assert "__init__" not in C2.__dict__
        assert "__init__" not in C3.__dict__

    def test_repr(self):
        @dataclass(repr=True)
        class C1:
            x: float = 1

        @dataclass(repr=False)
        class C2:
            x: float = 1

        assert "__repr__" in C1.__dict__
        assert "__repr__" not in C2.__dict__

    def test_eq(self):
        @dataclass(eq=True)
        class C1:
            x: float = 1

        @dataclass(eq=False)
        class C2:
            x: float = 1

        assert "__eq__" in C1.__dict__
        assert "__eq__" not in C2.__dict__

    def test_order(self):
        try:

            @dataclass(order=True, eq=False)
            class C:  # type: ignore
                x: float = 1

        except ValueError:
            assert True

    def test_unsafe_hash(self):
        @dataclass(eq=True, frozen=True)
        class C1:
            x: float = 1

        @dataclass(eq=True, frozen=False)
        class C2:
            x: float = 1

        @dataclass(eq=False, frozen=False)
        class C3:
            X: float = 1

        try:

            @dataclass(unsafe_hash=True)
            class C4:  # type: ignore
                x: float = 1

                def __hash__(self) -> int:
                    return hash(self.x)

        except TypeError:
            assert True

        assert "__hash__" in C1.__dict__
        assert C1.__dict__["__hash__"] is not None
        assert "__hash__" in C2.__dict__
        assert C2.__dict__["__hash__"] is None
        assert C3().__hash__() is not C1().__hash__()

    def test_inst_var(self):
        @dataclass()
        class C:
            x: float = 4

        a = C(6)
        assert a.x == 6

    def test_class_var(self):
        @dataclass()
        class C:
            x: ClassVar[int] = 4

        assert C.x == 4

    def test_classvar_without_typing(self):
        @dataclass()
        class C:
            x = 4

        assert C.x == 4

    def test_asdict(self):
        @dataclass
        class C:
            x: float = 1

        assert asdict(C()) == {"x": 1}

    def test_astuple(self):
        @dataclass
        class C:
            x: float = 1

        assert astuple(C()) == (1,)

    def test_replace(self):
        @dataclass(frozen=True)
        class C:
            x: float = 1
            y: float = field(default_factory=int)

        c = C()
        changes = {"x": 3, "y": 4}
        c1 = replace(c, **changes)

        assert c1.x == 3
        assert c1.y == 4

    def test_is_dataclass(self):
        @dataclass
        class C:
            x: float = 1

        assert is_dataclass(C())

    def test_frozen(self):
        @dataclass(frozen=True)
        class C:
            x: float = 1

        c = C()
        try:
            c.x = 2  # type: ignore
        except FrozenInstanceError:
            assert True

        C.x = 5

        assert C.x == 5
        assert c.x == 1
