class Room(object):

    def __init__(self, number=None):
        self.number = number
        self.adjascent_rooms = set()

    def get_adjascent(self):
        return self.adjascent_rooms

    def get_number(self):
        return self.number

    def add_adjascent(self, room):
        self.adjascent_rooms.add(room)
        room.adjascent_rooms.add(self)



