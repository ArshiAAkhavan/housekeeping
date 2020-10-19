import os
from os import path
from collections import namedtuple
import time

from house.cycle import Cycle

class Action:
    def __init__(self,command):
        self.command=command

Actions = namedtuple('Actions', 'pre_script post_script on_fail_script')

class Room:
    def __init__(self,name,path,cycles,actions):
        self.name=name
        self.path=path
        self.cycles=cycles
        self.actions=actions
        self.files=[]
        
        #very very important
        self.cycles=sorted(self.cycles,key=lambda c:c.value)
        self.cycles.reverse()
        # [print(c) for c in self.cycles]

    def load_all_files(self):    
        temp=[path.join(self.path, f) for f in os.listdir(self.path) if path.isfile(path.join(self.path, f))]
        files=sorted([(file,os.stat(file)[8]) for file in temp],key=lambda t:t[1])#returns creation time
        files.reverse()
        return files
    
    def get_all_excess_files(self):
        files=self.load_all_files()
        will_remain=set()
        for cycle in self.cycles:
            # print(cycle.name)
            now=int(time.time())
            deadline=now-cycle.value.bound
            for p,t in files:
                if t < now :
                    # print(f"now:{now}deadline:{deadline}")
                    # print(f"{p}:{t}")
                    will_remain.add(p)
                    now-=cycle.value.unit
                    if now<=deadline:
                        break
            print(will_remain)


        return list(set([p for p,t in files]).difference(will_remain))
    