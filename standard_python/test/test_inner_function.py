from typing import Any, Iterable, Union


class TestInnerFunction:
    def test_abs(self):
        assert abs(-3) == 3
        assert abs(3) == 3
        assert abs(-3.0) == 3.0
        assert 3 is not 3.0
        assert 3 == 3.0

    def test_all(self):
        assert not 0
        assert not None
        assert not all([1, 2, 3, 4, 5, None])
        assert not all([1, 2, 3, 4, 0])
        assert all({1: 1})
        assert all([])
        assert all(())
        assert all({})

    def test_any(self):
        assert any([1, 1])

    def test_ascii(self):
        assert ascii(1) == "1"

    def test_bin(self):
        assert bin(3) == "0b11"

    def test_bool(self):
        assert bool(1)
        assert not bool(0)

    def test_bytearray(self):
        assert bytearray("a", encoding="utf-8") == b"a"

    def test_bytes(self):
        assert bytearray("a", encoding="utf-8") == b"a"

    def test_callable(self):
        class C:
            def __call__(self, *args: Any, **kwds: Any) -> Any:
                ...

        c = C()
        assert callable(c)

    def test_chr(self):
        assert chr(8364) == "€"
        assert chr(97) == "a"

    def test_delattr(self):
        class C:
            def __new__(cls: Any):
                instance = super().__new__(cls)
                instance.x = 1

                return instance

            def __init__(self) -> None:
                self.y = 2

        c = C()
        assert c.__dict__ == {"x": 1, "y": 2}
        delattr(c, "x")
        assert c.__dict__ == {"y": 2}

    def test_dir(self):
        class C:
            def __dir__(self) -> Iterable[str]:
                return ["a", "b", "c"]

        assert dir(C()) == ["a", "b", "c"]

    def test_enumerate(self):
        seasons = ["spring", "summer", "fall", "winter"]

        assert list(enumerate(seasons)) == [(0, "spring"), (1, "summer"), (2, "fall"), (3, "winter")]

    def test_eval(self):
        try:
            eval("abs(-1)", {"__builtins__": None})
        except TypeError:
            assert True

    def test_exec(self):
        a = eval("10+10")
        exec("y=a")

        assert a == 20

        # TODO: assert y == 2

    def test_filter(self):
        def f(x: Union[float, int]) -> bool:
            if isinstance(x, float):
                return False

            return True

        assert list(filter(f, [1, 1.0, 2, 3.0])) == [1, 2]
        assert tuple(filter(f, [1, 1.0, 2, 3.0])) == (1, 2)

    def test_float(self):
        assert isinstance(float("inf"), float)
        assert float(1) == 1.0
        assert float() == 0.0

    def test_format(self):
        assert "one is {}".format(1) == f"one is {1}"

    def test_frozenset(self):
        assert len(frozenset([1, 2, 2, 1])) == 2

    def test_getattr(self):
        class A:
            def __init__(self) -> None:
                self.a = 1

        assert getattr(A(), "a") == 1

    def test_globals(self):
        assert isinstance(globals(), dict)

    def test_hasattr(self):
        class A:
            def __init__(self) -> None:
                self.a = 1

        assert hasattr(A(), "a")

    def test_hash(self):
        assert hash(1) == hash(1.0)

    def test_help(self):
        assert help(int) == None

    def test_hex(self):
        assert hex(255) == "0xff"

    def test_id(self):
        # CPython implementation detail: This is the address of the object in memory.
        assert id(1) == id(1)

    def test_input(self, monkeypatch: Any):
        monkeypatch.setattr("builtins.input", lambda _: "Mark")  # type: ignore

        i = input("What is your name?")
        assert i == "Mark"

    def test_int(self):
        assert int() == 0
        assert int(1) == 1
        assert int(1.0) == 1
        assert int("1") == 1
        assert int("0xA", base=16) == 10

    def test_isinstance(self):
        class A:
            ...

        assert isinstance(A, type)
        assert isinstance(A(), (A, type))

    def test_issubclass(self):
        class A:
            ...

        assert issubclass(A, object)

    def test_iter(self):
        try:
            len(range(2 ** 100))
        except (OverflowError):
            assert True

    def test_list(self):
        assert list() == []

    def test_locals(self):
        assert isinstance(locals(), dict)

    def test_map(self):
        assert list(map(lambda x: x * 2, [1, 2, 3])) == [2, 4, 6]

    def test_max(self):
        assert max([1, 2, 3]) == 3
        assert max(["a", "b", "c"]) == "c"

    def test_memoryview(self):
        v = memoryview(b"abcefg")
        assert v[1] == 98

    def test_min(self):
        assert min([1, 2, 3]) == 1
        assert min(1, 2) == 1

    def test_next(self):
        ...

    def test_object(self):
        o = object()
        assert not hasattr(o, "__dict__")

    def test_oct(self):
        assert oct(8) == "0o10"

    def test_ord(self):
        assert ord("a") == 97

    def test_pow(self):
        assert pow(2, 2) == 4

    def test_print(self):
        assert True

    def test_property(self):
        class C:
            def __init__(self):
                self._x = 1

            @property
            def x(self):
                """I'm the 'x' property."""
                return self._x

        assert C().x == 1

    def test_range(self):
        assert range(8)[0] == 0

    def test_repr(self):
        class C:
            def __repr__(self) -> str:
                return "C"

        assert repr(C()) == "C"

    def test_reversed(self):
        l = [1, 2, 3]
        assert list(reversed(l))[0] == 3

    def test_round(self):
        assert round(4.4) == 4

    def test_set(self):
        assert len(set([1, 1, 2, 2, 3, 3])) == 3

    def test_setattr(self):
        class C:
            ...

        c = C()
        setattr(c, "a", 1)
        assert c.a == 1  # type: ignore

    def test_slice(self):
        l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        assert l[slice(5)] == [0, 1, 2, 3, 4]

    def test_sorted(self):

        assert sorted([1, 2, 3], reverse=True) == [3, 2, 1]

    def test_staticmethod(self):
        ...

    def test_str(self):
        assert str("aaa") == "aaa"

    def test_sum(self):
        assert sum([1, 2, 3]) == 6

    def test_super(self):
        class B:
            def method(self):
                return 1

        class C(B):
            def method(self):
                return super().method()

        assert C().method() == 1

    def test_tuple(self):
        assert tuple(range(3)) == (0, 1, 2)

    def test_type(self):
        assert type(1) == int

    def test_vars(self):
        assert isinstance(vars(), dict)

    def test_zip(self):
        l1 = [1, 2, 3]
        l2 = ["a", "b", "c"]

        assert dict(zip(l1, l2)) == {1: "a", 2: "b", 3: "c"}

    def test_import(self):
        ...
