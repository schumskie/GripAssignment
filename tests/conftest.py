import pytest

from record import Action, Device, Record


@pytest.fixture()
def generic_records():
    return [
        Record(1, Device.windows_10, Action.start, 100),
        Record(2, Device.osx_154, Action.start, 200),
        Record(1, Device.iphone_8s, Action.start, 250),
        Record(1, Device.windows_10, Action.end, 370),
        Record(1, Device.iphone_8s, Action.end, 410),
        Record(2, Device.osx_154, Action.end, 490),
        Record(3, Device.andorid_91, Action.start, 700),
        Record(3, Device.andorid_91, Action.end, 850),
    ]


@pytest.fixture()
def spread_records():
    return [
        Record(1, Device.windows_10, Action.start, 100),
        Record(1, Device.windows_10, Action.end, 200),
        Record(1, Device.iphone_8s, Action.start, 250),
        Record(1, Device.iphone_8s, Action.end, 350),
        Record(1, Device.iphone_8s, Action.start, 450),
        Record(1, Device.iphone_8s, Action.end, 550),
    ]


@pytest.fixture()
def densed_records():
    return [
        Record(1, Device.windows_10, Action.start, 100),
        Record(1, Device.iphone_8s, Action.start, 200),
        Record(1, Device.iphone_8s, Action.end, 250),
        Record(1, Device.windows_10, Action.end, 350),
    ]


@pytest.fixture()
def mixed_records():
    return [
        Record(1, Device.windows_10, Action.start, 100),
        Record(1, Device.iphone_8s, Action.start, 200),
        Record(1, Device.iphone_8s, Action.end, 250),
        Record(1, Device.windows_10, Action.end, 350),
        Record(1, Device.andorid_91, Action.start, 380),
        Record(1, Device.osx_154, Action.start, 390),
        Record(1, Device.andorid_91, Action.end, 400),
        Record(1, Device.osx_154, Action.end, 430),
    ]
