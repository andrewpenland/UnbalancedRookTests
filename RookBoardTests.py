import unittest
from rookboard import RookBoard

# This suite tests the functions necessary for a Rook Board.
# The Board has one thing to keep track of: the position of the rook (as an integer tuple)
# The Board has one job: update itself given a player move, using the update(player_move_ function.

class RookBoardTests(unittest.TestCase):

    def test_update(self):
        the_board = RookBoard((5,5))
        player_move_1 = ("D",1)
        the_board.update(player_move_1)
        self.assertEqual(the_board.state, (0,1))
        player_move_2 = ("R", 2)
        self.assertEqual(the_board.state,(2,1))
        player_move_3 = ("D",2)
        self.assertEqual(the_board.state, (2,3))
        player_move_4 = ("R", 2)
        self.assertEqual(the_board.state, (4,3))
        player_move_5 = ("D",2)
        self.assertEqual(the_board.state, (4,5)) #the referee tests legality


if __name__ == '__main__':
    unittest.main()
