
import os

import requests
from dotenv import load_dotenv


def get_currency_conversion(transaction: dict) -> float:
    """Функция принимает на вход словарь с информацией о транзакции. Возвращает сумму транзакции в рублях. Поддерживает валюты
    RUB, USD, EUR"""
    load_dotenv(".env")
    apikey = os.getenv("API_KEY")
    payload = {}
    headers = {"apikey": apikey}
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])
    if currency == "RUB":
        return amount
    elif currency == "USD" or currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        responce = requests.request("GET", url, headers=headers, data=payload)
        result = responce.json().get("result")
        return result
    else:
        raise ValueError("неподходящая валюта для конвертации")


print(
    get_currency_conversion(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "1.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
)

print(
    get_currency_conversion(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )
)
