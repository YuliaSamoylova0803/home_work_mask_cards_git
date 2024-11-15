import pytest
from src.masks import get_mask_card_number


@pytest.fixture
def number_card():
    return "7000 79** **** 6361"

@pytest.mark.parametrize("number_card, expected", [("7000 79** **** 6361", "7000 79** **** 6361"),])
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected


def test_get_mask_card_empty():
    assert get_mask_card_number("") == " ** **** "