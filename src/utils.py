import json
import logging
import os

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)

# Создаем путь до файла JSON относительно текущей директории
rel_src_file_path = os.path.join(current_dir, "../data/operations.json")
abs_src_file_path = os.path.abspath(rel_src_file_path)

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_data(path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла со списком словарей и возвращает список словарей,
    как объект python. Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    returned_lict_data = []
    try:
        logging.info(f"Получение данных из файла {path}")
        with open(path, encoding="utf-8") as file_operations:
            dict_transaction_data = json.load(file_operations)
            if isinstance(dict_transaction_data, list):
                returned_lict_data = dict_transaction_data
    finally:
        logger.info("Импортируемый список записан.")
        return returned_lict_data


print(get_transaction_data(abs_src_file_path))
