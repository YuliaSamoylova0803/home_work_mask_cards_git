import pytest
from src.decorators import log


@log(filename="my_logs.txt")
def my_function(x: int , y: int ) -> int:
    """Функция суммирует два числа и возвращает результат"""
    return x + y

def test_log_save_file():
    result = my_function(2, 2)
    assert result == 4


def test_log_console_ok(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok"


def test_crash_log() -> None:
    with pytest.raises(TypeError, match="unsupported operand type(s) for +: 'int' and 'str'"):
        my_function(1, "a")


def test_log_captured(capsys) -> None:
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"