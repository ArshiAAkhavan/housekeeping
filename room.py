import os
from os import path

from collections import namedtuple


Actions = namedtuple('Actions', 'pre_script post_script on_fail_script')

class Room:
    def __init__(self,path,regex,cycles,actions):
        self.path=path
        self.regex=regex
        self.cycles=cycles
        self.actions=actions
        self.files=[]
        #very very important
        self.cycles.sort()
        self.load_all_files()

    def load_all_files(self):    
        self.files = [path.join(path, f) for f in os.listdir(path) if path.isfile(path.join(path, f))]
        
    def clean(self):
        for cycle in self.cycles:
            
