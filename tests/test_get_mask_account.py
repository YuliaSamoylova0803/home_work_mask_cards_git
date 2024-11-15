import pytest
from src.masks import get_mask_account


@pytest.fixture
def account_number():
    return "**6295"

@pytest.mark.parametrize("account_number, expected", [("**6295", "**6295"),])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_empty():
    assert get_mask_account("") == "**"