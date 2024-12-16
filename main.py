import os

from src.csv_pandas import get_csv_data, get_excel_data
from src.external_api import get_currency_conversion
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transaction_data
from src.widget import get_date, mask_account_card
from src.servise import counter_descriptions, search_operation_by_str

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))


# Создаем путь до файла JSON относительно текущей директории
rel_src_file_path = os.path.join(current_dir, '/data/operations.json')
abs_src_file_path = os.path.abspath(rel_src_file_path)

# Создаем путь до файла CSV относительно текущей директории
rel_src_file_path_csv = os.path.join(current_dir, "../data/transactions.csv")
abs_src_file_path_csv = os.path.abspath(rel_src_file_path_csv)

# Создаем путь до файла CSV относительно текущей директории
rel_src_file_path_xlsx = os.path.join(current_dir, "../data/transactions_excel.xlsx")
abs_src_file_path_xlsx = os.path.abspath(rel_src_file_path_xlsx)



def main() -> None:
    """Функция, которая отвечает за основную логику проекта с пользователем и связывает функциональности между собой"""

    print('Приветствую! Добро пожаловать в программу работы с банковскими транзакциями. \nВыберите необходимый пункт меню:\n'
          '1. Получить информацию о тракзакциях из JSON-файла.\n'
          '2. Получить информацию о тракзакциях из CSV-файла.\n'
          '3. Получить информацию о тракзакциях из XLSX-файла')

    user_input_file_type = input('Введите номер пункта: ')
    if user_input_file_type == '1':
        print('Файл будет выведен в формате JSON')
        transactions_file_from = get_transaction_data('\\data\\operations.json')
    elif user_input_file_type == '2':
        print('Файл будет выведен в формате CSV')
        transactions_file_from = get_csv_data('\\data\\transactions.csv')
    elif user_input_file_type == '3':
        print('Файл будет выведен в формате XLSX')
        transactions_file_from = get_excel_data('\\data\\transactions_excel.xlsx')
    else:
        print('Введен некорректный номер')
        print(transactions_file_from)


    # while True:
    #     print('Введите статус, по которому необходимо выполнить фильтрацию.\n'
    #          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
    #     user_input_state = input('Введите статус для фильтрации: ').upper()
    #     if user_input_state in ['PENDING', 'CANCELED', 'EXECUTED']:
    #         break
    #     else:
    #         print(f'Статус операции {user_input_state} недоступен')
    # filtred = filter_by_state(transactions_file_from, user_input_state)
    # print(f'Операции отфильтрованы по статусу {user_input_state}')
    # print(filtred)
    #
    # while True:
    #     print('Отсортировать операции по дате?')
    #     users_sort_by_date = input('Введите "да" или "нет": ').lower()
    #     if users_sort_by_date in ("да", "нет"):
    #         break
    #     else:
    #         print("Введён некорректный ответ. Повторите ввод ответа.")
    #     if users_sort_by_date == "да":
    #         print('Отсортировать по возрастанию или по убыванию?')
    #         filter = input('по возрастанию/по убыванию: ').lower()
    #         if filter == 'по возрастанию':
    #             sorted_list_dict = sort_by_date(filtred, True)
    #         elif filter == 'по убыванию':
    #             sorted_list_dict = sort_by_date(filtred, False)
    #         else:
    #             print('\nОшибка ввода.\n Попробуйте ввести еще раз.\n')
    #             break
    #     elif filter == 'нет':
    #         sorted_list_dict = filtred
    #         return
    #     else:
    #         print('\nОшибка ввода!\nПопробуйте ещё раз.\n ')
    #
    # while True:
    #     print('Выводить только рублевые транзакции? Да/Нет')
    #     users_choise_rub = input('Введите "да" или "нет": ').lower()
    #     if users_choise_rub in ('да', 'нет'):
    #         break
    #     else:
    #         print('Введён некорректный ответ. Повторите ввод ответа.')
    # if users_choise_rub == "да":
    #     rub_transactions = []
    #     for transact in sorted_list_dict:
    #         if user_input_file_type == '1' or user_input_file_type == '2':
    #             if transact['operationAmount']['currency']['code'] == 'RUB':
    #                 rub_transactions.append(transact)
    #         else:
    #             if transact['currency_code'] == 'RUB':
    #                 rub_transactions.append(transact)
    # elif users_choise_rub == 'нет':
    #     rub_trans = []
    #     for trans in sorted_list_dict:
    #         rub_trans.append(trans)
    # else:
    #     print("Введен некорректный ответ.")
    #     return

    # Фильтрация по определённому слову в описании



















print(main())

# print(get_mask_card_number(""))
# print(get_mask_account("45652659515194526295"))
# print(get_date("2024-03-11T02:26:18.671407"))
# print(mask_account_card("Visa Platinum 7000792289606361"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 35383033474447895560"))
# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
# usd_transactions = filter_by_currency(
#     (
#         [
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702",
#             },
#             {
#                 "id": 142264268,
#                 "state": "EXECUTED",
#                 "date": "2019-04-04T23:20:05.206878",
#                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 19708645243227258542",
#                 "to": "Счет 75651667383060284188",
#             },
#             {
#                 "id": 873106923,
#                 "state": "EXECUTED",
#                 "date": "2019-03-23T01:09:46.296404",
#                 "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 44812258784861134719",
#                 "to": "Счет 74489636417521191160",
#             },
#             {
#                 "id": 895315941,
#                 "state": "EXECUTED",
#                 "date": "2018-08-19T04:27:37.904916",
#                 "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "Перевод с карты на карту",
#                 "from": "Visa Classic 6831982476737658",
#                 "to": "Visa Platinum 8990922113665229",
#             },
#             {
#                 "id": 594226727,
#                 "state": "CANCELED",
#                 "date": "2018-09-12T21:27:25.241689",
#                 "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#                 "description": "Перевод организации",
#                 "from": "Visa Platinum 1246377376343588",
#                 "to": "Счет 14211924144426031657",
#             },
#         ]
#     ),
#     "USD",
# )
# for _ in range(3):
#     print(next(usd_transactions))
# print(
#     filter_by_currency(
#         (
#             [
#                 {
#                     "id": 939719570,
#                     "state": "EXECUTED",
#                     "date": "2018-06-30T02:08:58.425572",
#                     "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#                     "description": "Перевод организации",
#                     "from": "Счет 75106830613657916952",
#                     "to": "Счет 11776614605963066702",
#                 },
#                 {
#                     "id": 142264268,
#                     "state": "EXECUTED",
#                     "date": "2019-04-04T23:20:05.206878",
#                     "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#                     "description": "Перевод со счета на счет",
#                     "from": "Счет 19708645243227258542",
#                     "to": "Счет 75651667383060284188",
#                 },
#                 {
#                     "id": 873106923,
#                     "state": "EXECUTED",
#                     "date": "2019-03-23T01:09:46.296404",
#                     "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#                     "description": "Перевод со счета на счет",
#                     "from": "Счет 44812258784861134719",
#                     "to": "Счет 74489636417521191160",
#                 },
#                 {
#                     "id": 895315941,
#                     "state": "EXECUTED",
#                     "date": "2018-08-19T04:27:37.904916",
#                     "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#                     "description": "Перевод с карты на карту",
#                     "from": "Visa Classic 6831982476737658",
#                     "to": "Visa Platinum 8990922113665229",
#                 },
#                 {
#                     "id": 594226727,
#                     "state": "CANCELED",
#                     "date": "2018-09-12T21:27:25.241689",
#                     "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#                     "description": "Перевод организации",
#                     "from": "Visa Platinum 1246377376343588",
#                     "to": "Счет 14211924144426031657",
#                 },
#             ]
#         )
#     )
# )
#
# print(filter_by_currency([]))
# usd_transactions = filter_by_currency([], "")
# for _ in range(0):
#     print(next(usd_transactions))
# descriptions = transaction_descriptions(
#     [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188",
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160",
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229",
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657",
#         },
#     ]
# )
#
#
# for _ in range(5):
#     print(next(descriptions))
#     print(
#         transaction_descriptions(
#             [
#                 {
#                     "id": 939719570,
#                     "state": "EXECUTED",
#                     "date": "2018-06-30T02:08:58.425572",
#                     "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#                     "description": "Перевод организации",
#                     "from": "Счет 75106830613657916952",
#                     "to": "Счет 11776614605963066702",
#                 },
#                 {
#                     "id": 142264268,
#                     "state": "EXECUTED",
#                     "date": "2019-04-04T23:20:05.206878",
#                     "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#                     "description": "Перевод со счета на счет",
#                     "from": "Счет 19708645243227258542",
#                     "to": "Счет 75651667383060284188",
#                 },
#                 {
#                     "id": 873106923,
#                     "state": "EXECUTED",
#                     "date": "2019-03-23T01:09:46.296404",
#                     "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#                     "description": "Перевод со счета на счет",
#                     "from": "Счет 44812258784861134719",
#                     "to": "Счет 74489636417521191160",
#                 },
#                 {
#                     "id": 895315941,
#                     "state": "EXECUTED",
#                     "date": "2018-08-19T04:27:37.904916",
#                     "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#                     "description": "Перевод с карты на карту",
#                     "from": "Visa Classic 6831982476737658",
#                     "to": "Visa Platinum 8990922113665229",
#                 },
#                 {
#                     "id": 594226727,
#                     "state": "CANCELED",
#                     "date": "2018-09-12T21:27:25.241689",
#                     "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#                     "description": "Перевод организации",
#                     "from": "Visa Platinum 1246377376343588",
#                     "to": "Счет 14211924144426031657",
#                 },
#             ]
#         )
#     )
# card_number = card_number_generator(start=1, end=5)
# for card_number in card_number_generator(1, 5):
#     print(card_number)
#
#
# print(get_transaction_data(path="data/operations.json"))
# print(get_transaction_data(path="data/empty.json"))
# print(get_transaction_data(path="data/dict.json"))
#
# print(
#     get_currency_conversion(
#         {
#             "id": 441945886,
#             "state": "EXECUTED",
#             "date": "2019-08-26T10:50:58.294041",
#             "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#             "description": "Перевод организации",
#             "from": "Maestro 1596837868705199",
#             "to": "Счет 64686473678894779589",
#         }
#     )
# )
#
#
# print(get_csv_data(path_csv="data/transactions.csv"))
# print(get_csv_data(path_csv="data/empty.json"))
#
# print(get_excel_data("data/transactions_excel.xlsx"))
# print(get_excel_data(path_excel="data/none.json"))
