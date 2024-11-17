import pytest

from src.masks import get_mask_account
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number_str_1, expected",
    [
        ("Счет 35383033474447895560", "**5560"),
        ("Счет 64686473678894779589", "**9589"),
        ("Счет 73654108430135874305", "**4305"),
    ],
)
def test_mask_account_card(number_str_1, expected):
    assert get_mask_account(number_str_1) == expected


@pytest.mark.parametrize(
    "number_str, expected",
    [
        ("Visa Platinum 7000792289606361", "**6361"),
        ("MasterCard 7158300734726758", "**6758"),
        ("Maestro 1596837868705199", "**5199"),
        ("Visa Classic 6831982476737658", "**7658"),
        ("Visa Gold 5999414228426353", "**6353"),
    ],
)
def test_mask_account_card(number_str, expected):
    assert get_mask_account(number_str) == expected


def test_mask_account_empty() -> None:
    assert mask_account_card("") == "Строка пуста"


@pytest.mark.parametrize("number_str", [("Visa Platinum "), ("Счет "), ("Visa Platinum AAAAAAAAAAAAAAAA")])
def test_mask_account_card_number_error(number_str: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(number_str)


@pytest.mark.parametrize(
    "data_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-03-11T02:26:18.671407", "11.03.2022"),
        ("2024-05-12T02:26:18.671407", "12.05.2024"),
    ],
)
def test_get_date(data_str: str, expected: str) -> None:
    assert get_date(data_str) == expected


def test_get_date_empty() -> None:
    assert get_date("") == "Строка пуста"


def test_get_date_invalid_data() -> None:
    with pytest.raises(ValueError):
        get_date("20/12/2023")
