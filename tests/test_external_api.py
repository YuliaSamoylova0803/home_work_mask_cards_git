from unittest.mock import Mock, patch

import pytest

from src.external_api import get_currency_conversion


@patch("requests.get")
def test_get_currency_conversion_rub(transaction_rub):
    mock_response = Mock()
    mock_response.json.return_value == 31957.58


@patch("requests.get")
def test_get_currency_conversion_usd(transaction_usd):
    mock_response = Mock()
    mock_response.json.return_value == 838520.225503


def test_get_currency_conversion_error_gbp():
    with pytest.raises(ValueError):
        get_currency_conversion(
            {
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "GBP"}},
                "description": "Открытие вклада",
                "to": "Счет 41421565395219882431",
            }
        )
