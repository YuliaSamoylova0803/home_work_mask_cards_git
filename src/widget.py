from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_str: str) -> str:
    """Возвращать строку с замаскированным номером.
    Для карт и счетов используйте разные типы маскировки.
    Visa Platinum 7000792289606361  # входной аргумент
    Visa Platinum 7000 79** **** 6361  # выход функции
    Счет 73654108430135874305  # входной аргумент
    Счет **4305  # выход функции"""

    if number_str == "":
        return "Строка пуста"
    else:
        original_number = number_str.split()[-1]
        if original_number.isdigit():
            if len(original_number) == 16:
                card_number_1 = get_mask_card_number(original_number)
                result = f"{number_str[:-16]}{card_number_1}"
            elif len(original_number) == 20:
                card_number_2 = get_mask_account(original_number)
                result = f"{number_str[:-20]}{card_number_2}"
            return result
        else:
            raise ValueError("Неверный формат")

#print(mask_account_card(""))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("Visa Platinum 8990922113665229"))


def get_date(data_str: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"  и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"  ("11.03.2024")."""
    return f"{data_str[8:10]}.{data_str[5:7]}.{data_str[:4]}"
