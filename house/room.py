import os
from os import path
from collections import namedtuple
import time
import subprocess
import logging as logger
from house.cycle import Cycle

class Action:
    def __init__(self,command):
        self.command=command
    
    def run(self):
        cmd = subprocess.Popen(self.command)
        cmd.communicate()
        if cmd.returncode == 0:
            logger.info("command exited with exitcode 0")
        else:
            logger.warning(f"something went wrong! exitcode: {cmd.returncode}")


Actions = namedtuple('Actions', 'pre_script post_script on_fail_script')

OS_STAT_CTIME=8

class Room:
    def __init__(self,name,path,cycles,actions):
        self.name=name
        self.path=path
        self.cycles=cycles
        self.actions=actions
        self.files=[]
        
        self.cycles=sorted(self.cycles,key=lambda c:c.value)
        self.cycles.reverse()

    def load_all_files(self):    
        temp=[path.join(self.path, f) for f in os.listdir(self.path) if path.isfile(path.join(self.path, f))]
        files=sorted([(file,os.stat(file)[OS_STAT_CTIME]) for file in temp],key=lambda t:t[1])#returns creation time
        files.reverse()
        return files
    
    def get_all_excess_files(self):
        logger.warning(f"room:{self.name}\t====> running pre script")
        if self.actions.pre_script:
            self.actions.pre_script.run()
        try:
            files=self.load_all_files()
            will_remain=set()
            for cycle in self.cycles:
                now=int(time.time())
                deadline=now-cycle.value.bound
                for p,t in files:
                    if t < now :
                        will_remain.add(p)
                        now-=cycle.value.unit
                        if now<=deadline:
                            break
            will_be_delted=list(set([p for p,t in files]).difference(will_remain))
            logger.warning(f"room:{self.name}\t====> running post script")
            if self.actions.post_script:
                self.actions.post_script.run()
            return will_be_delted
        except Exception:
            logger.warning(f"room:{self.name}\t====> failed assessing the excess files")
            logger.warning(f"room:{self.name}\t====> running on_fail script")
            if self.actions.post_script:
                self.actions.post_script.run()
        