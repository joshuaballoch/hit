import unittest
from cave import Cave

class CaveTest(unittest.TestCase):

    def test_it_has_an_entrace(self):
        cave = Cave()
        self.assertIsNotNone(cave.entrance)

    # things to want:
    #    cycles
    #


    # Possible tests:
    #   1. one room has wumpus
    #   2. 1+ rooms are pits
    #    -> are these responsibilities of Cave?

if __name__ == '__main__':
    unittest.main()
