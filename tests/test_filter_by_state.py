import pytest
from src.processing import filter_by_state


@pytest.fixture
def list_dict():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

@pytest.mark.parametrize("list_dict, state, expected", [
    (list_dict,"state='EXECUTED'",
      [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])}
    # (list_dict,"state='CANCELED'",
    #   [
    #     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}])

def test_filter_by_state(list_dict, state, expected):
    assert filter_by_state(list_dict, state) == expected


def test_filter_by_state_empty():
    assert filter_by_state([]) == []


# def test_filter_by_state_invalid_lict():
#     with pytest.raises(ValueError):
#         filter_by_state(list_dict)
import pytest

@pytest.fixture
def test_transactions():
    return transactions

@pytest.fixture
def test_initial_list():
    return 'EXECUTED'

@pytest.fixture
def test_initial_list_1():
    return list_dict

from src.processing import filter_by_state, sort_by_date, initial_list


def test_filter_by_state(list_dict):
    assert filter_by_state(initial_list, state=test_initial_list)


def test_filter_by_state_1(test_initial_list_1):
    assert filter_by_state(list_dict) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

def test_filter_by_state_sort(test_initial_list_1):
    assert sort_by_date(list_dict) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]