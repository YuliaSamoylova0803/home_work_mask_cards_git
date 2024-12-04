from typing import List, Any
import json

# load_dotenv('.env')


def get_transaction_data(path: str) -> list[dict]:
    """ Функция принимает на вход путь до JSON-файла со списком словарей и возвращает список словарей, как объект python.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    returned_lict_data = []
    try:
        with open(path, encoding='utf-8') as file_operations:
            dict_transaction_data = json.load(file_operations)
            if isinstance(dict_transaction_data, list):
                returned_lict_data = dict_transaction_data
    finally:
        return returned_lict_data





#print(get_transaction_data(path='data/operations.json'))
