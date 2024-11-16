import pytest

from src.widget import get_date


@pytest.fixture
def data_str():
    return "11.03.2024"

@pytest.mark.parametrize("data_str, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                                ("2022-03-11T02:26:18.671407", "11.03.2022"),
                                                  ("2024-05-12T02:26:18.671407", "12.05.2024"),])
def test_get_date(data_str, expected):
    assert get_date(data_str) == expected


def test_get_date_empty():
    assert get_date("") == "Строка пуста"


def test_get_date_invalid_data():
    with pytest.raises(ValueError):
        get_date("2024-03-11T02:26:18671407")