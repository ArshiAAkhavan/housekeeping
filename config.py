import os
import yaml

from house.room import Room,Action,Actions
from house.cycle import Cycle,CycleTuple
from house.house import House
import logging as logger


def parse_config(path):
    config=None
    with open(path, 'r') as stream:
        try:
            config=yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config

def get_rooms(path):
    room_paths = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    rooms=[]
    for r in room_paths:
        cfg=parse_config(os.path.join(path, r))
        cfg=(cfg,{})[cfg==None]
######################################## Pattern ############################################
        if not "pattern"in cfg:cfg["pattern"]=".*"

######################################## Actions ############################################
        pre,post,fail=None,None,None
        if "actions" in cfg:
            if "pre_script" in cfg["actions"]: pre=Action(cfg["actions"]["pre_script"])
            if "post_script" in cfg["actions"]: post=Action(cfg["actions"]["post_script"])
            if "on_fail_script" in cfg["actions"]: fail=Action(cfg["actions"]["on_fail_script"])
        actions=Actions(pre,post,fail)

######################################## Cycles ############################################
        cycles=[]
        if "cycles" in cfg:
            for cycle in cfg["cycles"]:
                if type(cycle)== dict:
                    c=list(cycle.keys())[0]
                    cycles.append(CycleTuple(cycle[c]["unit"],cycle[c]["bound"]))
                else: cycles.append(Cycle[cycle].value)
            # cycles=[Cycle[cycle] for cycle in cfg["cycles"]]
        else:
            cycles=[c.value for c in Cycle]     
        try:
            rooms.append(Room(r,cfg["path"],cfg["pattern"],cycles,actions))
        except Exception:
            logger.error(f"path must be specified for room:{r}")
            raise SystemExit
            
    return rooms

def get_houses(house_prefix):
    house_paths=[d for d in os.listdir(house_prefix) if os.path.isdir(os.path.join(house_prefix,d))]
    return [House(house_path,get_rooms(os.path.join(house_prefix, house_path)))for house_path in house_paths]

config=""
def parse(config_path):
    config=parse_config(config_path)
    return get_houses(config["house-directories"])
    # return House(get_rooms(config["house-directory"]))
