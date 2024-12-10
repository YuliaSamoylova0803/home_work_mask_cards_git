import os
import csv
import pandas as pd


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла cvs относительно текущей директории
rel_src_file_path = os.path.join(current_dir, "../data/transactions.csv")
abs_src_file_path = os.path.abspath(rel_src_file_path)

def get_csv_data(path_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    returned_lict = []

    try:
        with open(path_csv) as file_save_csv:
            reader_dict_csv = csv.DictReader(file_save_csv, delimiter=";")
            return list(reader_dict_csv)

    except FileNotFoundError:
        return []


print(get_csv_data(abs_src_file_path))
print(get_csv_data(path_csv="data/empty.json"))