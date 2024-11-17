import pytest


@pytest.fixture
def number_card():
    return "7000792289606361"


@pytest.fixture
def account_number():
    return "45652659515194526295"


@pytest.fixture
def number_str():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def number_str_1():
    return "Счет 64686473678894779589"


@pytest.fixture
def data_str():
    return "11.03.2024"
