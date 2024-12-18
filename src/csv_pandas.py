import os

import pandas as pd

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))
rel_src_file_path = os.path.join(current_dir, "../data/transactions.csv")
abs_src_file_path = os.path.abspath(rel_src_file_path)


def get_csv_data(path_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""

    try:
        transactions_df = pd.read_csv(path_csv, delimiter=";", encoding="utf-8")
        result = transactions_df.to_dict(orient="records")
        return result

    except FileNotFoundError:
        return []
    except Exception:
        return []


# print(get_csv_data(abs_src_file_path))
# print(get_csv_data(path_csv="data/empty.json"))


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла cvs относительно текущей директории
rel_src_file_path1 = os.path.join(current_dir, "../data/transactions_excel.xlsx")
abs_src_file_path1 = os.path.abspath(rel_src_file_path1)


def get_excel_data(path_excel: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями."""
    try:
        df = pd.read_excel(path_excel)
    except FileNotFoundError:
        return []
    excel_data = df.to_dict(orient="records")
    return excel_data


# print(get_excel_data(abs_src_file_path1))
