from dataclasses import dataclass
from enum import Enum


class Action(str, Enum):
    start = "start"
    end = "end"


class Device(str, Enum):
    windows_10 = "Windows 10"
    iphone_8s = "Iphone 8s"
    andorid_91 = "Android 9.1"
    osx_154 = "OSX 15.4"


@dataclass
class Record:
    user_id: int
    device: str
    action: Action
    date_actioned: int
