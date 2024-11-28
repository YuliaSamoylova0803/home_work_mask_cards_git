from functools import wraps
from time import time
from typing import Optional, Callable, Any


def log(filename: Optional[str]=None) -> Callable:
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции
    """

    def logging_decorator(func):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)

                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
                return result

            except Exception as error:
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__}error:{error.class.name}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__}error:{error.class.name}. Inputs: {args}, {kwargs}")
            finally:
                print(f"Выходим из функции: {func.__name__}")
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


"""def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.debug(f'Входим в функцию: {func.__name__}')
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Произошла ошибка в {func.__name__}', exc_info=True)
            raise
        finally:
            logger.debug(f'Выходим из функции: {func.__name__}')
    return wrapper"""
