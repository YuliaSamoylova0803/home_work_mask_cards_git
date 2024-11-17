import pytest
from src.widget import mask_account_card, get_date
from src.masks import get_mask_account


@pytest.mark.parametrize("number_str_1, expected", [("Счет 35383033474447895560", "**5560"),
                                                ("Счет 64686473678894779589", "**9589"),
                                                  ("Счет 73654108430135874305", "**4305"),])
def test_mask_account_card(number_str_1, expected):
    assert get_mask_account(number_str_1) == expected


@pytest.mark.parametrize("number_str, expected", [("Visa Platinum 7000792289606361", "**6361"),
                                                ("MasterCard 7158300734726758", "**6758"),
                                                  ("Maestro 1596837868705199", "**5199"),
                                                    ("Visa Classic 6831982476737658", "**7658"),
                                                    ("Visa Gold 5999414228426353", "**6353")])
def test_mask_account_card(number_str, expected):
    assert get_mask_account(number_str) == expected


def test_mask_account_empty():
    assert mask_account_card("") == "Строка пуста"


def test_mask_account_invalid_number():
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum AAAAAAAAAAAAAAAA")

