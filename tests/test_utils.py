import os

from src.utils import get_transaction_data

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))
rel_src_file_path = os.path.join(current_dir, "../data/operations.json")
abs_src_file_path = os.path.abspath(rel_src_file_path)


def test_get_trancsaction_data(list_json):
    assert get_transaction_data(rel_src_file_path) == list_json


def test_get_c():
    assert get_transaction_data("data\\empty.json") == []


def test_get_trancsaction_data_incorrect_data():
    assert get_transaction_data("\\data\\dict.json") == []


def test_get_trancsaction_data_incorrect_path():
    assert get_transaction_data("\\data\\none.json") == []
