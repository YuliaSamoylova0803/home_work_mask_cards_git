from collections.abc import Generator, Iterator
from typing import Any, Dict, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str = "USD") -> Generator[Dict[str, Any]]:
    """Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    if len(transactions) > 0:
        filtered_transactions = filter(
            lambda transactions: transactions.get("operationAmount").get("currency").get("code") == currency,
            transactions,
        )
        return filtered_transactions
    else:
        return "Список пустой!"


def transaction_descriptions(transactions: List[Dict[Any, Any]]) -> Iterator[None]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for description in transactions:
        yield description["description"]


# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start: int, end: int) -> Generator[str, Any]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X
    — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999. Генератор должен принимать начальное
    и конечное значения для генерации диапазона номеров."""
    for number in range(start, end):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"

    # for card_number in card_number_generator(1, 9999999999999999):
    #     return card_number
