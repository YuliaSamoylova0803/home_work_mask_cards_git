from collections.abc import generator
from unittest import expectedFailure

import pytest

from main import descriptions
from src.generators import filter_by_currency
from tests.conftest import transactions
from src.generators import card_number_generator
from src.generators import transaction_descriptions


def test_filter_by_currency(transactions, currency: str= "USD"):
    usd_transactions = filter_by_currency(transactions)
    # for _ in range(2):
    #     print(next(usd_transactions))

    assert next(usd_transactions) == {
            'id': 939719570,
             'state': 'EXECUTED',
             'date': '2018-06-30T02:08:58.425572',
             'operationAmount': {'amount': '9824.07',
                                 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации',
             'from': 'Счет 75106830613657916952',
             'to': 'Счет 11776614605963066702'
    }
    assert next(usd_transactions) == {
        'id': 142264268,
        'state': 'EXECUTED',
        'date': '2019-04-04T23:20:05.206878',
        'operationAmount': {'amount': '79114.93',
                            'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Перевод со счета на счет',
        'from': 'Счет 19708645243227258542',
        'to': 'Счет 75651667383060284188'
    }
    assert next(usd_transactions) == {
        'id': 895315941,
        'state': 'EXECUTED',
        'date': '2018-08-19T04:27:37.904916',
        'operationAmount': {'amount': '56883.54',
                            'currency': {'name': 'USD', 'code': 'USD'}},
        'description': 'Перевод с карты на карту',
        'from': 'Visa Classic 6831982476737658',
        'to': 'Visa Platinum 8990922113665229'
    }

def test_filter_by_currency_empty():
    usd_transactions = filter_by_currency([], "")
    with pytest.raises(TypeError):
        filter_by_currency()


def test_card_number_generator(start, end) -> str:
    card_number = card_number_generator(1, 9999999999999999)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"


#@pytest.mark.parametrize("expected", ["Перевод организации"])
def test_transaction_descriptions(transactions):
    trans = transaction_descriptions(transactions)
    assert next(trans) == "Перевод организации"
    assert next(trans) == "Перевод со счета на счет"
    assert next(trans) == "Перевод со счета на счет"
    assert next(trans) == "Перевод с карты на карту"
    assert next(trans) == "Перевод организации"