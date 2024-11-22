from collections.abc import Generator
from typing import List, Dict, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str="USD" ) -> List[Dict[str, Any]]:
    """Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    if transactions == []:
        raise TypeError == ("Транзакции в заданной валюте отсутствуют")
    elif transactions != []:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["name"] == currency:
                yield transaction

# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))


def transaction_descriptions(transactions: List[Dict[Any, Any]]) -> Generator[int, None, None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for description in transactions:
        yield description["description"]


# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))

def card_number_generator(card_number_start: str, card_number_stop: str)-> Generator[str, Any]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X
 — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
 от 0000 0000 0000 0001 до 9999 9999 9999 9999. Генератор должен принимать начальное
 и конечное значения для генерации диапазона номеров."""
    pass




