def get_mask_card_number(number_card: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску
    в формате XXXX XX** **** XXXX"""
    return f"{number_card[:4]} {number_card[5:7]}** **** {number_card[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску
    в формате **XXXX"""
    account_mask = f"**{account_number[-4:]}"
    return account_mask
