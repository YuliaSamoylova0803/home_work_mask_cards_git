from typing import List, Dict, Any


def filter_by_state(list_dict: List[Dict[str, Any]], state: str ='EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению."""
    new_list_dict = []
    for i in list_dict:
        if i.get("state") == state:
            new_list_dict.append(i)
    return new_list_dict


def sort_by_date(list_dict: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате (date)"""
    sorted_list_dict = []
    sorted_list_dict = sorted(list_dict, key=lambda x: x["date"], reverse=reverse)
    return sorted_list_dict
