import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card


@pytest.fixture
def number_str():
    return "Visa Platinum 7000 79** **** 6361"

@pytest.mark.parametrize("number_str, expected", [("Visa Platinum 7000 79** **** 6361", "**6361"),
                                                ("Счет 64686473678894779589", "**9589"),
                                                  ("Maestro 1596837868705199", "**5199"),])
def test_mask_account_card(number_str, expected):
    assert get_mask_account(number_str) == expected


def test_mask_account_empty():
    assert mask_account_card("") == "Строка пуста"


def test_mask_account_invalid_number():
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum AAAAAAAAAAAAAAAA")