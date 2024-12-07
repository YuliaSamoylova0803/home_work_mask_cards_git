import logging
import os

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(rel_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску
    в формате XXXX XX** **** XXXX"""
    logger.info("Формат карты верный")
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску
    в формате **XXXX"""
    logger.info("Формат счета верный")
    account_mask = f"**{account_number[-4:]}"
    return account_mask
