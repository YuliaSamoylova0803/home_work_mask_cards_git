from src.utils import get_transaction_data


def test_get_trancsaction_data(list_json):
    assert (
        get_transaction_data(
            "C:\\Users\\Юлия Самойлова\\PycharmProjects\\pythonProject\\home_work_mask_cards_git\\data\\operations.json"
        )
        == list_json
    )


def test_get_trancsaction_data_empty():
    assert (
        get_transaction_data(
            "C:\\Users\\Юлия Самойлова\\PycharmProjects\\pythonProject\\home_work_mask_cards_git\\data\\empty.json"
        )
        == []
    )


def test_get_trancsaction_data_incorrect_data():
    assert (
        get_transaction_data(
            "C:\\Users\\Юлия Самойлова\\PycharmProjects\\pythonProject\\home_work_mask_cards_git\\data\\dict.json"
        )
        == []
    )


def test_get_trancsaction_data_incorrect_path():
    assert (
        get_transaction_data(
            "C:\\Users\\Юлия Самойлова\\PycharmProjects\\pythonProject\\home_work_mask_cards_git\\data\\none.json"
        )
        == []
    )
