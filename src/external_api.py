import os
from json import JSONDecodeError
from unittest.mock import patch

import requests
from dotenv import load_dotenv

from utils import get_transaction_data


def get_currency_conversion(transaction: list[str, str|float]) -> float:
    """Функция принимает на вход словарь с информацией о транзакции. Возвращает сумму транзакции в рублях. Поддерживает валюты
    RUB, USD, EUR"""
    load_dotenv(".env")
    apikey = os.getenv("API_KEY")
    headers = {"apikey": apikey}
    empty_file: list = []

    if type(transaction) is list:
        try:
            for i in transaction:
                amount_str = float(i["operationAmount"]["amount"])
                if i["operationAmount"]["currency"]["code"] == "RUB":
                    return amount_str
                else:
                    url = f"https://api.apilayer.com/exchangerates_data/convert?from=USD&to=RUB&amount={amount_str}"
                    responce = requests.get(url, headers=headers)
                    result = responce.json()
                    if type(result) is dict:
                        return result["result"]
        except JSONDecodeError:
            print(empty_file)
            return amount_str


if __name__ == "__main__":
    file = "C:\\Users\\Юлия Самойлова\\PycharmProjects\\pythonProject\\home_work_mask_cards_git\\data\\operations.json"
    json_file = get_transaction_data(file)
    print(get_currency_conversion(json_file))
