from enum import Enum

hour = 1000*60*60


class Cycle(Enum):
    HOURLY = hour*1
    DAILY = hour*24
    WEEKLY = hour*24*7
    MONTHLY = hour*24*30
    YEARLY = hour*24*365


# file="/home/kycilius/Documents/Code/Python/housekeeping/room.py"
# import os, time
# ctime= os.stat(file)[9]
# mtime= os.stat(file)[8]
# print(os.stat(file))
# print("creation date: %s" % time.ctime(ctime))
# print("last modified: %s" % time.ctime(mtime))
