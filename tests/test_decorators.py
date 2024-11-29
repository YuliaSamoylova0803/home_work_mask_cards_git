import pytest
from src.decorators import log, my_function


def test_log_save_file():
    result = my_function(2, 2)
    assert result == 4


def test_log_console_ok(capsys):
    return my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_crash_log() -> None:
    with pytest.raises(ValueError, match="invalid literal for int() with base 10: 'a'"):
        my_function()


def test_log_captured(capsys) -> None:
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"