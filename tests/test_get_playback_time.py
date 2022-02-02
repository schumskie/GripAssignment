from assignments import get_playback_time


def test_get_playback_time_generic(generic_records):
    assert get_playback_time(1, generic_records) == 310


def test_get_playback_time_for_separate_timespans(spread_records):
    assert get_playback_time(1, spread_records) == 300


def test_get_playback_time_for_densed_records(densed_records):
    assert get_playback_time(1, densed_records) == 250


def test_get_playback_time_for_mixed_records(mixed_records):
    assert get_playback_time(1, mixed_records) == 300
