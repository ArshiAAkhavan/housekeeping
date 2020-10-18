class House:
    def __init__(self, rooms):
        self.rooms = rooms

    def keep(self):
        [room.clean() for room in self.rooms]

    def keep_room(self, room_name):
        try:
            filter(lambda r: r.name == room_name, self.rooms).__next__().clean()
        except StopIteration:
            pass
    
    def add_room(self,room):
        self.rooms.append(room)
    
