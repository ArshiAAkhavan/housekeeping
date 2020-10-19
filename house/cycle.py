from enum import Enum
from collections import namedtuple

CycleTuple = namedtuple('CycleTuple', 'unit bound')

hour = 3600
class Cycle(Enum):
    HOURLY = CycleTuple(hour*1, hour*24)
    DAILY  = CycleTuple(hour*24, hour*24*7)
    WEEKLY = CycleTuple(hour*24*7, hour*24*30)
    MONTHLY= CycleTuple(hour*24*30, hour*24*365)
    YEARLY = CycleTuple(hour*24*365,float("inf"))


# file="/home/kycilius/Documents/Code/Python/housekeeping/room.py"
# import os, time
# ctime= os.stat(file)[9]
# mtime= os.stat(file)[8]
# print(os.stat(file))
# print("creation date: %s" % time.ctime(ctime))
# print("last modified: %s" % time.ctime(mtime))
