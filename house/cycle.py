from enum import Enum

hour=1000*60*60
class cycle(Enum):
    HOUR=hour*1
    DAY=hour*24
    WEEK=hour*24*7
    MONTH=hour*24*30
    YEAR=hour*24*365


# file="/home/kycilius/Documents/Code/Python/housekeeping/room.py"
# import os, time
# ctime= os.stat(file)[9]
# mtime= os.stat(file)[8]
# print(os.stat(file))
# print("creation date: %s" % time.ctime(ctime))
# print("last modified: %s" % time.ctime(mtime))
