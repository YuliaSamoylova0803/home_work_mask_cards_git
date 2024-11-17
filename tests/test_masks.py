import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number(number_card: str, expected: str) -> None:
    assert get_mask_card_number(number_card) == expected


def test_get_mask_card_empty(number_card: str) -> None:
    assert get_mask_card_number("") == " ** **** "


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("45652659515194526295", "**6295"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_account_empty() -> None:
    assert get_mask_account("") == "**"
