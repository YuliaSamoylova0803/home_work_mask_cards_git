from typing import List, Any
import json

# load_dotenv('.env')


def get_list_dict_with_financial_transaction_data(file_operations) -> List:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    with open('data/operations.json', encoding='utf-8') as file_operations:
        data = json.load(file_operations)
        return data



# print(get_list_dict_with_financial_transaction_data(file_operations='data/operations.json'))
