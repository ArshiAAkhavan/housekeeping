from enum import Enum
from collections import namedtuple

CycleTuple = namedtuple('CycleTuple', 'unit bound')

hour = 3600
class Cycle(Enum):
    HOURLY = CycleTuple(hour*1,     hour*24)
    DAILY  = CycleTuple(hour*24,    hour*24*7)
    DAILY_M= CycleTuple(hour*24,    hour*24*30)
    WEEKLY = CycleTuple(hour*24*7,  hour*24*30)
    MONTHLY= CycleTuple(hour*24*30, hour*24*365)
    YEARLY = CycleTuple(hour*24*365,float("inf"))
