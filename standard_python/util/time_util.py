from typing import Any, Callable
from functools import wraps
import time


def timer(fn: Callable[..., Any]) -> Callable[..., Any]:
    @wraps
    def wrapper(*args: Any, **kargs: Any) -> Any:
        print(f"开始执行{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        result = fn(args, kargs)
        print(f"执行完毕{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        return result

    return wrapper


def format_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


__all__ = ["timer", "format_time"]  # type: ignore
