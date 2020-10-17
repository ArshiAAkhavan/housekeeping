import os
from os import path
import yaml



def parse_config(path):
    with open(path, 'r') as stream:
        try:
            config=yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config

def get_rooms(path):
    room_paths = [path.join(path, f) for f in os.listdir(path) if path.isfile(path.join(path, f))]
    map(,room_paths)


config=""

def init(config_path):
    config=parse_config(config_path)
    get_rooms(config["house-directory"])