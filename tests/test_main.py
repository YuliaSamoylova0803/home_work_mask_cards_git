
from unittest.mock import patch


@patch("main.input")
def test_main_1(mock_input):
    mock_input.return_value = "Файл будет выведен в формате JSON"


@patch("main.input")
def test_main_2(mock_input):
    mock_input.return_value = "Операции отфильтрованы по статусу CANCELED"


@patch("main.input")
def test_main_3(mock_input):
    mock_input.return_value = "Отсортировать по возрастанию или по убыванию?"


@patch("main.input")
def test_main_4(mock_input):
    mock_input.return_value = "Выводить только рублевые транзакции? Да/Нет"


@patch("main.input")
def test_main_5(mock_input):
    mock_input.return_value = "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"


@patch("main.input")
def test_main_6(mock_input):
    mock_input.return_value = "Распечатываю итоговый список транзакций..."


# @patch('main.sort_by_word_yes')
# @patch('main.user_search')
# @patch('main.users_sort_by_date')
# @patch('main.users_choice_rub')
# @patch('main.user_input_state')
# @patch('main.user_input_file_type')
# def test_main_7(mock_file_type, mock_state, mock_choice_rub, mock_sort_by_date, mock_user_search, mock_word_yes):
#     mock_file_type.return_value = '1'
#     mock_state.return_value = 'CANCALED'
#     mock_choice_rub.return_value = 'да'
#     mock_sort_by_date.return_value = 'НА КАРТУ'
#     mock_user_search.return_value = 'да'
#     mock_word_yes.return_value = ''

# assert main() == []


# @patch('src.main.user_search_word')
# @patch('src.main.user_sort_option')
# @patch('src.main.user_state_select')
# @patch('src.main.user_file_select')
# def test_main(mock_file_select, mock_stat_select, mock_sort_option, mock_user_search_word):
#     mock_file_select.return_value = '2'
#     mock_stat_select.return_value = 'CANCALED'
#     mock_sort_option.return_value = 'ДА'
#     mock_user_search_word.return_value = 'НА КАРТУ'
#     assert main() == []
