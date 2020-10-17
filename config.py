import os
import yaml

from house.room import Room,Action,Actions


def parse_config(path):
    config=None
    with open(path, 'r') as stream:
        try:
            config=yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config

def get_rooms(path):
    room_paths = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    rooms=[]
    for r in room_paths:
        cfg=parse_config(r)
        actions=Actions(Action(cfg["actions"]["pre_script"]),Action(cfg["actions"]["post_script"]),Action(cfg["actions"]["on_fail_script"]))
        rooms.append(Room(cfg["path"],cfg["cycles"],actions))
    return rooms

config=""
def init(config_path):
    config=parse_config(config_path)
    return get_rooms(config["house-directory"])
