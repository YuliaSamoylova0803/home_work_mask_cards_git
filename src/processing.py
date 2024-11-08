from typing import List, Dict, Any


def filter_by_state(list_dict: List[Dict[str, Any]], state='EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], содержащий только те словари, у которых ключ
state соответствует указанному значению."""
    new_list_dict = []
    for i in list_dict:
        if i.get("state") == state:
            new_list_dict.append(i)
    return new_list_dict


def sort_by_date(list_dict: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате (date)"""
