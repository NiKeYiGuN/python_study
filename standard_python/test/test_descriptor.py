from standard_python.validator import Number, OneOf, String
from typing import Any, Union


class TestDescriptor:
    def test_const(self):
        class D:
            def __get__(self, obj: Any, objtype: Any = None):
                return 10

        class A:
            x = 5
            d = D()

        a = A()

        assert a.x == 5
        assert a.d == 10
        assert A.x == 5
        assert A.d == 10

    def test_dynamic(self):
        class D:
            def __get__(self, obj: Any, objtype: Any = None) -> int:
                return len(obj.name)

        class A:
            d = D()
            name = "1"

            def __init__(self, name: str):
                self.name = name

        a1 = A("s")
        assert a1.d == 1
        a2 = A("ss")
        assert a2.d == 2

    def test_managed_property(self):
        class D:
            def __get__(self, obj: Any, objtype: Any = None) -> int:
                return obj._age

            def __set__(self, obj: Any, value: Any):
                # return setattr(obj, obj._age, value)
                obj._age = value

        class A:
            age = D()

            def __init__(self, *, name: str = "xiaoming", age: int = 11):
                self.name = name
                self.age = age  # Call __set__(self=age, obj=a, value=11)

        a = A()
        assert "_age" in a.__dict__
        assert a.age == 11
        assert a._age == 11  # type: ignore

    def test_set_name(self):
        class D:
            def __set_name__(self, owner: Any, name: str):
                self.public_name = name
                self.private_name = f"_{name}"

            def __get__(self, obj: Any, objtype: Any = None):
                return getattr(obj, self.private_name)

            def __set__(self, obj: Any, value: Any):
                setattr(obj, self.private_name, value)

        class A:
            name = D()
            age = D()

            def __init__(self, name: str = "xm", age: int = 11):
                self.name = name
                self.age = age

            def birthday(self):
                self.age += 1

        a = A()
        assert vars(vars(A)["age"]) == {"public_name": "age", "private_name": "_age"}
        assert vars(a) == {"_name": "xm", "_age": 11}
        assert "_age" in vars(a)
        assert "_name" in vars(a)
        assert "age" not in vars(a)
        assert "name" not in vars(a)
        a.birthday()
        assert a.age == 12

    def test_validator(self):
        class Coponent:
            name = String(min_size=3, max_size=20, predicate=str.isupper)
            kind = OneOf(["wood", "metal", "plastic"])
            quantity = Number(min_value=0)

            def __init__(self, *, name: str, kind: str, quantity: Union[int, float]) -> None:
                self.name = name
                self.kind = kind
                self.quantity = quantity

        cls_var = Coponent.__dict__["name"]
        descr_get = getattr(type(cls_var), "__get__", None)
        assert descr_get is not None

        c = Coponent(name="lx", kind="wood", quantity=2)
        assert vars(vars(Coponent)["name"]) == {
            "min_size": 3,
            "max_size": 20,
            "predicate": str.isupper,
            "public_name": "name",
            "private_name": "_name",
        }
        assert c.name == "lx"
        assert c.kind == "wood"
        assert c.quantity == 2
