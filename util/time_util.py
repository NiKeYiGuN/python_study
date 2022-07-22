from typing import Any, Callable
from functools import wraps
import time
import datetime


def timer(fn: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = datetime.datetime.now()
        print(f"start:{start_time}")
        result = fn(*args, **kwargs)
        ent_time = datetime.datetime.now()
        print(f"end:{ent_time}")
        print(fn.__name__, "execute time:", f"{ent_time-start_time}")
        return result

    return wrapper


def format_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


__all__ = ["timer", "format_time"]  # type: ignore
