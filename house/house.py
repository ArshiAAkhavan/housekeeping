import os
class House:
    def __init__(self, rooms):
        self.rooms = rooms

    def keep(self,dry_run=False):
        excess_files=[]
        [excess_files.append((room.name,self.__keep_room(room,dry_run))) for room in self.rooms]
        return excess_files

    def __keep_room(self, room,dry_run):
        excess_files=room.get_all_excess_files()
        if dry_run: [os.remove(p) for p in excess_files]
        return excess_files
    
    def add_room(self,room):
        self.rooms.append(room)
    
