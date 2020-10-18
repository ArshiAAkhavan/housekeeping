import os
import yaml

from house.room import Room,Action,Actions
from house.cycle import Cycle
from house.house import House


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
        pre,post,fail=None,None,None
        if "pre_script" in cfg["actions"]: pre=Action(cfg["actions"]["pre_script"])
        if "post_script" in cfg["actions"]: post=Action(cfg["actions"]["post_script"])
        if "on_fail_script" in cfg["actions"]: fail=Action(cfg["actions"]["on_fail_script"])
        actions=Actions(pre,post,fail)
        # actions=Actions(Action(cfg["actions"]["pre_script"]),Action(cfg["actions"]["post_script"]),Action(cfg["actions"]["on_fail_script"]))
        cycles=[Cycle[cycle] for cycle in cfg["cycles"]]
        rooms.append(Room(r,cfg["path"],cycles,actions))
    return rooms

config=""
def parse(config_path):
    config=parse_config(config_path)
    return House(get_rooms(config["house-directory"]))
