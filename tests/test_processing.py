from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import list_dict_incorrect_date


def test_filter_by_state_default_value(list_dict: List[Dict[str, Any]], state: str = 'EXECUTED') -> None:
    assert filter_by_state(list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_value_canceled(list_dict: List[Dict[str, Any]], state: str = 'EXECUTED') -> None:
    assert filter_by_state(list_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_without_requested_state(list_dict: List[Dict[str, Any]], state: str = 'EXECUTED') -> None:
    assert filter_by_state(list_dict, "None") == []


def test_filter_by_state_empty() -> None:
    assert filter_by_state([]) == []


def test_sort_by_date(list_dict: List[Dict[str, Any]], reverse: bool = True) -> None:
    assert sort_by_date(list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_reverse(list_dict: List[Dict[str, Any]], reverse: bool = True) -> None:
    assert sort_by_date(list_dict, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_invalid_data(list_dict: List[Dict[str, Any]], reverse: bool = True) -> None:
    with pytest.raises(TypeError):
        sort_by_date(list_dict_incorrect_date)
