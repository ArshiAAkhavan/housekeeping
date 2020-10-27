import os
from os import path
from collections import namedtuple
import time
import subprocess
import logging as logger
from house.cycle import Cycle
import concurrent.futures
import re
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
    def __init__(self,name,path,pattern,cycles,actions):
        self.name=name
        self.path=path
        self.pattern = re.compile(pattern)
        self.cycles=cycles
        self.actions=actions
        self.files=[]
        
        self.cycles=sorted(self.cycles)
        self.cycles.reverse()

    def load_all_files(self):    
        temp=[path.join(self.path, f) for f in os.listdir(self.path) if self.pattern.match(f) and path.isfile(path.join(self.path, f))]
        files=sorted([(file,os.stat(file)[OS_STAT_CTIME]) for file in temp],key=lambda t:t[1])#returns creation time
        files.reverse()
        return files
    def clean(self,excess_files):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results= executor.map(self.delete,excess_files)
            if sum(r for r in results) >0:
                logger.warning(f"room:{self.name}\t====> deleting phase failed due to some errors")
                logger.warning(f"room:{self.name}\t====> some excess file may already be there")
                return 

            logger.warning(f"room:{self.name}\t====> running post script")
            if self.actions.post_script:
                self.actions.post_script.run()
            
    def delete(self,path):
        try:
            os.remove(path) 
            logger.warning(f"room:{self.name}\t====> file {path} deleted")
            return 0
        except Exception:
            logger.warning(f"room:{self.name}\t====> failed assessing the excess files")
            logger.warning(f"room:{self.name}\t====> running on_fail script")
            if self.actions.post_script:
                self.actions.post_script.run()
            return 1

    def get_all_excess_files(self):
        ##################### logging ###############################
        logger.warning(f"room:{self.name}\t====> running pre script")
        if self.actions.pre_script:
            self.actions.pre_script.run()
        ##################### logging ###############################
        try:
            files=self.load_all_files()
            will_remain=set()
            for cycle in self.cycles:
                now=int(time.time())
                deadline=now-cycle.bound
                for p,t in files:
                    if t < deadline:continue
                    if t < now :
                        will_remain.add(p)
                        now-=cycle.unit
                        if now<=deadline:
                            break
                        
            return list(set([p for p,t in files]).difference(will_remain))
        except Exception:
            ################################ logging ###################################
            logger.warning(f"room:{self.name}\t====> failed assessing the excess files")
            logger.warning(f"room:{self.name}\t====> running on_fail script")
            if self.actions.post_script:
                self.actions.post_script.run()
            ################################ logging ###################################
