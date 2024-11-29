from fileinput import filename

import pytest
from src.decorators import log, my_function


def test_log_save_file():
    result = my_function(2, 2)
    assert result == 4


def test_log_console_ok(capsys):
    return my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_captured(capsys) -> None:
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_in_file() -> None:
    @log(filename="log.txt")
    def my_function(x:int, y:int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y
    my_function(2, 2)
    with open("log.txt") as f:
        data = f.read().split("\n")[-2]
    assert data == "my_function ok"


# def test_error_handling(capsys):
#     with pytest.raises(TypeError):
#         my_function(1, 'a')
#         print("Ошибка ввода! Пожалуйста, вводите только целые числа.")
#     # captured = capsys.readouterr()
#     # assert  captured.out == None
#
#
#
# def test_crash_log() -> None:
#     with pytest.raises(Exception, match="invalid literal for int() with base 10: 'a'"):
#         my_function()


def test_log_invalid_type() -> None:
    @log(filename="log.txt")
    def my_function(x:int, y:int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y
    my_function(1, "а")
    with open("log.txt") as f:
        data = f.read().split("\n")[-2]
    assert data == "my_function error: TypeError. Inputs: (1, 'а'), {}"



    def test_log_empty(capsys) -> None:
        @log(filename=None)
        def my_function(x: int, y: int) -> int:
            """Функция суммирует два числа и возвращает результат"""
            return x + y

        my_function()
        captured = capsys.readouterr()
        assert captured.out ==