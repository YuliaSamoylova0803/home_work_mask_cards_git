from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который может логировать работу функции и ее результат как в файл, так и в консоль."""

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

        return wrapper

    return logging_decorator


@log(filename="my_logs.txt")
def my_function(x: int | str, y: int | str) -> int:
    """Функция суммирует два числа и возвращает результат"""
    try:
        return int(x) + int(y)
    except ValueError as e:
        print("Ошибка ввода! Пожалуйста, вводите только целые числа.")
        raise e


my_function(1, "123")
# print(my_function(1,2))
