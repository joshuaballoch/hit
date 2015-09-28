import unittest
from room import Room

class RoomTest(unittest.TestCase):

    def test_get_number(self):
        room = Room(5)
        self.assertEqual(room.get_number(), 5)

    def test_set_adjascent_room_adds_room(self):
        room_one = Room(1)
        room_two = Room(2)
        room_one.add_adjascent(room_two)

        self.assertEqual(room_one.get_adjascent().pop(), room_two)

    def test_set_adjascent_room_is_bidirectional(self):
        room_one = Room(1)
        room_two = Room(2)
        room_one.add_adjascent(room_two)

        self.assertEqual(room_two.get_adjascent().pop(), room_one)

if __name__ == '__main__':
    unittest.main()
