import os

from src.csv_pandas import get_csv_data, get_excel_data
from src.processing import filter_by_state, sort_by_date
from src.servise import search_operation_by_str
from src.utils import get_transaction_data
from src.widget import get_date, mask_account_card

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))


# Создаем путь до файла JSON относительно текущей директории
rel_src_file_path = os.path.join(current_dir, "/data/operations.json")
abs_src_file_path = os.path.abspath(rel_src_file_path)

# Создаем путь до файла CSV относительно текущей директории
rel_src_file_path_csv = os.path.join(current_dir, "../data/transactions.csv")
abs_src_file_path_csv = os.path.abspath(rel_src_file_path_csv)

# Создаем путь до файла CSV относительно текущей директории
rel_src_file_path_xlsx = os.path.join(current_dir, "../data/transactions_excel.xlsx")
abs_src_file_path_xlsx = os.path.abspath(rel_src_file_path_xlsx)


def main() -> None:
    """Функция, которая отвечает за основную логику проекта с пользователем и связывает функциональности между собой"""

    print(
        """Приветствую! Добро пожаловать в программу работы с банковскими транзакциями. \nВыберите необходимый пункт меню:\n"
        "1. Получить информацию о тракзакциях из JSON-файла.\n"
        "2. Получить информацию о тракзакциях из CSV-файла.\n"
        "3. Получить информацию о тракзакциях из XLSX-файла
        """
    )

    user_input_file_type = input("Введите номер пункта: ")
    if user_input_file_type == "1":
        print("Файл будет выведен в формате JSON")
        transactions_file_from = get_transaction_data(
            "C:\\Users\\Юлия Самойлова\\PycharmProjects\\pythonProject\\home_work_mask_cards_git\\data\\operations.json"
        )

    elif user_input_file_type == "2":
        print("Файл будет выведен в формате CSV")
        transactions_file_from = get_csv_data(
            "C:\\Users\\Юлия Самойлова\\PycharmProjects\\pythonProject\\home_work_mask_cards_git\\data\\transactions.csv"
        )

    elif user_input_file_type == "3":
        print("Файл будет выведен в формате XLSX")
        transactions_file_from = get_excel_data(
            "C:\\Users\\Юлия Самойлова\\PycharmProjects\\pythonProject\\home_work_mask_cards_git\\data\\transactions_excel.xlsx"
        )

    else:
        print("Введен некорректный номер")
        return

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )

        user_input_state = input("Введите статус для фильтрации: ").upper()

        if user_input_state != "EXECUTED" and user_input_state != "CANCELED" and user_input_state != "PENDING":
            print(f"Статус операции {user_input_state} недоступен.")
            continue
        print(f"Операции отфильтрованы по статусу {user_input_state}")
        filtred_transaction_data = filter_by_state(transactions_file_from, user_input_state)
        break

    print("Отсортировать операции по дате?")
    users_sort_by_date = input('Введите "да" или "нет": ').lower()

    if users_sort_by_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_up_down = input("по возрастанию/по убыванию: ").lower()
        if user_input_up_down == "по возрастанию":
            sorted_list_dict = sort_by_date(filtred_transaction_data, False)
        elif user_input_up_down == "по убыванию":
            sorted_list_dict = sort_by_date(filtred_transaction_data, True)
        else:
            print("\nОшибка ввода.\n Попробуйте ввести еще раз.\n")
            return

    elif users_sort_by_date == "нет":
        sorted_list_dict = filtred_transaction_data
    else:
        print("\nОшибка ввода!\nПопробуйте ещё раз.\n ")
        return

    print("Выводить только рублевые транзакции? Да/Нет")
    users_choice_rub = input('Введите "да" или "нет": ').lower()

    if users_choice_rub == "да":
        rub_transactions = []
        for transact in sorted_list_dict:
            if user_input_file_type == "1" or user_input_file_type == "2":
                if transact.get("operationAmount").get("currency").get("code") == "RUB":
                    rub_transactions.append(transact)

            else:
                if transact["currency_code"] == "RUB":
                    rub_transactions.append(transact)

    elif users_choice_rub == "нет":
        rub_transactions = []
        for transact in sorted_list_dict:
            rub_transactions.append(transact)

    else:
        print("\nОшибка ввода!\nПопробуйте ещё раз.\n ")
        return

        # Фильтрация по определённому слову в описании
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_search = input("Введите да или нет: ").lower()

    if user_search == "да":
        sort_by_word_yes = input("Введите слово для фильтрации(Перевод организации(с карты на карту, с карты на счет,со счета на счет), Открытие счета): ").capitalize()
        transactions_word = search_operation_by_str(rub_transactions, sort_by_word_yes)

    elif user_search == "нет":
        transactions_word = []
        for trans in rub_transactions:
            transactions_word.append(trans)

    else:
        print("Введен некорректный ответ.")
        return
    if len(transactions_word) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(transactions_word)}\n ")

    for transaction in transactions_word:
        if transaction.get("from") and transaction.get("to"):
            date = get_date(transaction.get("date"))
            print(date)
            # bad_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
            # correct_date = bad_date.strftime('%d.%m.%Y')
            description = transaction.get("description", "")
            masked_card_from = mask_account_card(str(transaction.get("from")))
            masked_card_to = mask_account_card(str(transaction.get("to")))
            masked_acc_from = mask_account_card(str(transaction.get("from")))
            masked_acc_to = mask_account_card(str(transaction.get("to")))

        if user_input_file_type == "1":
            amount = transaction["operationAmount"]["amount"]
            if "Счет" in transaction.get("from", "") and "Счет" in transaction.get("to", ""):
                date = get_date(str(transaction.get("date")))
                description = transaction.get("description", "")
                masked_acc_to = mask_account_card(str(transaction.get("to")))
                masked_acc_from = mask_account_card(str(transaction.get("from")))
                print(f"{date} {description}")
                print(f"Счет {masked_acc_from} -> Счет {masked_acc_to}")
                if transaction.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f"Сумма: {amount} {transaction.get('operationAmount').get('currency').get('code')}\n")
            elif "Счет" in transaction.get("to", ""):
                date = get_date(str(transaction.get("date")))
                description = transaction.get("description", "")
                masked_acc_to = mask_account_card(str(transaction.get("to")))
                print(f"{date} {description}")
                print(f"Счет {masked_acc_to}")
                if transaction.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f"Сумма: {amount} {transaction.get('operationAmount').get('currency').get('code')}\n")
            else:
                amount = transaction["operationAmount"]["amount"]
                if "Счет" in str(transaction.get("from")) and "Счет" in str(transaction.get("to")):
                    date = get_date(str(transaction.get("date")))
                    description = transaction.get("description", "")
                    masked_acc_to = mask_account_card(str(transaction.get("to")))
                    masked_acc_from = mask_account_card(str(transaction.get("from")))
                    print(f"{date} {description}")
                    print(f"Счет {masked_acc_from} -> Счет {masked_acc_to}")
                    if transaction.get("code") == "RUB":
                        print(f"Сумма: {amount} руб.\n")
                    else:
                        print(f"Сумма: {amount} {transaction.get('currency_code')}")
                elif "Счет" in transaction.get("to", ""):
                    date = get_date(str(transaction.get("date")))
                    description = transaction.get("description", "")
                    masked_acc_to = mask_account_card(str(transaction.get("to")))
                    print(f"{date} {description}")
                    print(f"Счет {masked_acc_to}")
                    if transaction.get("code") == "RUB":
                        print(f"Сумма: {amount} руб.\n")
                    else:
                        print(f"Сумма: {amount} {transaction.get('currency_code')}")
                else:
                    date = get_date(str(transaction.get("date")))
                    description = transaction.get("description", "")
                    masked_card_from = mask_account_card(str(transaction.get("from")))
                    masked_card_to = mask_account_card(str(transaction.get("to")))
                    print(f"{date} {description}")
                    print(f"Транзакция {masked_card_from} -> {masked_card_to}")
                    if transaction.get("code") == "RUB":
                        print(f"Сумма: {amount} руб.\n")
                    else:
                        print(f"Сумма: {amount} {transaction.get('currency_code')}")

        #     # currency_name = transaction['operationAmount']['currency']['name']
        #     # print(f'Сумма: {amount} {currency_name}')
        # elif user_input_file_type == '2' or user_input_file_type == '3':
        #         amount = operation['amount']
        #         currency_name = operation['currency_name']
        #         print(f'Сумма: {amount} {currency_name}')
        # else:
        #     acc_number_from = mask_account_card(operation['from'])
        #     acc_number_to = mask_account_card(operation['to'])
        #     print(f'{acc_number_from} -> {acc_number_to}')
        #     if user_input_file_type == '1':
        #         amount = operation['operationAmount']['amount']
        #         currency_name = operation['operationAmount']['currency']['name']
        #         print(f'Сумма: {amount} {currency_name}')
        #     elif user_input_file_type == '2' or user_input_file_type == '3':
        #         amount = operation['amount']
        #         currency_name = operation['currency_name']
        #         print(f'Сумма: {amount} {currency_name}')


if __name__ == "__main__":
    result = main()
