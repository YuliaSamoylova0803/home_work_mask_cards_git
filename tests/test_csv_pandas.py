import os
from unittest.mock import patch

from src.csv_pandas import get_csv_data, get_excel_data

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла cvs относительно текущей директории
rel_src_file_path = os.path.join(current_dir, "../data/transactions.csv")
abs_src_file_path = os.path.abspath(rel_src_file_path)


def test_get_csv_data_empty():
    assert get_csv_data("data\\empty.json") == []


def test_get_cvs_data_incorrect_data():
    assert get_csv_data("\\data\\dict.json") == []


def test_get_csv_data_incorrect_path():
    assert get_csv_data("\\data\\none.json") == []


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла cvs относительно текущей директории
rel_src_file_path1 = os.path.join(current_dir, "../data/transactions_excel.xlsx")
abs_src_file_path1 = os.path.abspath(rel_src_file_path1)


def test_get_excel_data_incorrect_path():
    assert get_excel_data("\\data\\none.json") == []


@patch("pandas.read_csv")
def test_get_csv_data(mock_read_csv) -> None:
    """Тестирование функции считывания CSV-файла"""
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]
    result = get_csv_data("test_file_path.csv")
    assert result == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]


@patch("pandas.read_excel")
def test_get_excel_data(mock_read_excel) -> None:
    mock_read_excel.return_value.to_dict.return_value = [
        {"test_dict": "01", "test_key": "test_value_1"},
        {"test_dict": "02", "test_key": "test_value_2"},
    ]
    result = get_excel_data("test_file_path.xlsx")
    assert result == [{"test_dict": "01", "test_key": "test_value_1"}, {"test_dict": "02", "test_key": "test_value_2"}]
