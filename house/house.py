class House:
    def __init__(self,rooms):
        self.rooms=rooms

    def keep(self):
        [room.keep() for room in self.rooms]

    