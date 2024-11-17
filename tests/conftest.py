import pytest


@pytest.fixture
def number_card() -> str:
    return "7000792289606361"


@pytest.fixture
def account_number() -> str:
    return "45652659515194526295"


@pytest.fixture
def number_str() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def number_str_1()-> str:
    return "Счет 64686473678894779589"


@pytest.fixture
def data_str() -> str:
    return "11.03.2024"


@pytest.fixture
def list_dict() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_dict_incorrect_date() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
        {"id": 594226727, "state": "CANCELED", "date": "12/09/2017 21;42"},
        {"id": 615064591, "state": "CANCELED", "date": "четырнадцатое октября две тысячи восемнадцатого года"},
    ]
