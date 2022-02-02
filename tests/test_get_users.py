import pytest as pytest

from assignments import get_users
from record import Action


def test_get_users_generic(generic_records):
    assert get_users(generic_records, Action.start, 700, 900) == [3]


def test_get_users_do_not_find_records_ahead_of_timespan(generic_records):
    assert get_users(generic_records, Action.start, 880, 900) == []


def test_get_users_find_all_records(generic_records):
    assert sorted(get_users(generic_records, Action.start, 0, 900)) == [1, 2, 3]
