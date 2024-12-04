from typing import List, Any
import json

# load_dotenv('.env')


def get_list_dict_with_financial_transaction_data(file_operations) -> List[Any]:
    """Функция, возвращает список словарей с данными о финансовых транзакциях"""
    if file_operations is None:
        return []
    else:
        with open('data/operations.json', encoding='utf-8') as file_operations:
            dict_transaction_data = json.load(file_operations)
            return dict_transaction_data



print(get_list_dict_with_financial_transaction_data(file_operations='data/operations.json'))
