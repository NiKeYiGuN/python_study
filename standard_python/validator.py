from abc import ABC, abstractmethod
from typing import Any, Callable, List, Optional, Union


class Validator(ABC):
    def __set_name__(self, owner: Any, name: str) -> None:
        self.public_name = name
        self.private_name = f"_{name}"

    def __set__(self, obj: Any, value: str) -> None:
        setattr(obj, self.private_name, value)

    def __get__(self, obj: Any, objtype: Any) -> None:
        return getattr(obj, self.private_name)

    @abstractmethod
    def validate(self, value: Any) -> None:
        ...


class OneOf(Validator):
    def __init__(self, options: List[str]) -> None:
        self.options = set(options)

    def validate(self, value: Any) -> None:
        if value not in self.options:
            raise ValueError(f"Expected {value!r} to be one of {self.options!r}")


class Number(Validator):
    def __init__(
        self,
        min_value: Union[int, float, None] = None,
        max_value: Union[int, float, None] = None,
    ) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value: Any) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected {value!r} to be an int or float")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Expected {value!r} to be at least {self.min_value!r}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Expected {value!r} to be no more than {self.max_value!r}")


class String(Validator):
    def __init__(
        self,
        min_size: Optional[int] = None,
        max_size: Optional[int] = None,
        predicate: Optional[Callable[..., Any]] = None,
    ) -> None:
        self.min_size = min_size
        self.max_size = max_size
        self.predicate = predicate

    def validate(self, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Expected {value!r} to be an str")
        if self.min_size is not None and len(value) < self.min_size:
            raise ValueError(f"Expected {value!r} to be no smaller than {self.min_size!r}")
        if self.max_size is not None and len(value) > self.max_size:
            raise ValueError(f"Expected {value!r} to be no bigger than {self.max_size!r}")
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f"Expected {self.predicate} to be true for {value!r}")
