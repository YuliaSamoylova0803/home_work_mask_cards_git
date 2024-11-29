
from functools import wraps
from time import time
from typing import Optional, Callable, Any


def log(filename: Optional[str]=None) -> Callable:
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции
    """

    def logging_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}")
                raise error
        return wrapper
    return logging_decorator


def printing(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func} started")
        result = func(*args, **kwargs)
        print(f"Function {func} finished")
        return result
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f"Time for work: {time_2 - time_1}")
    return wrapper


@log(filename="my_logs.txt")
def my_function(x: int | str, y: int | str) -> int:
    """Функция суммирует два числа и возвращает результат"""
    return int(x) + int(y)

my_function(1, 2)
print(my_function(1,2))

