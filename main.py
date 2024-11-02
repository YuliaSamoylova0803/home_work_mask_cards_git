from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import get_date
from src.widget import mask_account_card



print(get_mask_card_number("7000792289606361"))
print(get_mask_account("45652659515194526295"))
print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 35383033474447895560"))