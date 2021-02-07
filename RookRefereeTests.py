import unittest
from rookreferee import RookReferee
from rookboard import RookBoard

# This suite tests the functions of a RookReferee
# The rook referee has two jobs:
#  1. Determine if a player's move is legal given a state of the board
#  2. Determine if a given state has resulted in winning the game
# Job 1 is implemented through the function is_legal(board_state, player_move)
# Job 2 is implemented through the function is_winning(board_state)

class RookRefereeTest(unittest.TestCase):

    def test_is_legal(self):
        the_board = RookBoard((4, 4)) #create board
        the_ref = RookReferee(the_board) #this statement and previous could be moved to a setUp function
        self.assertTrue(the_ref.is_legal((0, 0), ("D", 1)))
        self.assertTrue(the_ref.is_legal((0, 0), ("R", 3)))
        self.assertTrue(the_ref.is_legal((2, 1), ("R", 1)))
        self.assertTrue(the_ref.is_legal((2, 1), ("D", 2)))
        self.assertFalse(the_ref.is_legal((0, 0), ("D", 4)))
        self.assertFalse(the_ref.is_legal((0, 0), ("R", 4)))
        self.assertFalse(the_ref.is_legal((2, 1), ("D", 3)))
        self.assertFalse(the_ref.is_legal((2, 1), ("R", 2)))
        self.assertFalse(the_ref.is_legal((0, 0), ("R", 0)))
        self.assertFalse(the_ref.is_legal((0, 0), ("D", 0)))
        self.assertFalse(the_ref.is_legal((0, 0), ("R", -1)))
        self.assertFalse(the_ref.is_legal((0, 0), ("D", -1)))
        self.assertFalse(the_ref.is_legal((0, 0), ("R", 1.5)))
        self.assertFalse(the_ref.is_legal((0, 0), ("D", 1.5)))
        self.assertFalse(the_ref.is_legal((2, 1), ("R", -1)))
        self.assertFalse(the_ref.is_legal((2, 1), ("D", -1)))
        self.assertFalse(the_ref.is_legal((2, 1), ("R", 0.5)))
        self.assertFalse(the_ref.is_legal((2, 1), ("D", 0.5)))
        self.assertFalse(the_ref.is_legal((2, 1), ("A", 2)))

    def test_is_winning(self):
        the_board = RookBoard((4, 4))  # create board
        the_ref = RookReferee(the_board)  # this statement and previous could be moved to a setUp function
        self.assertTrue(the_ref.is_winning((3,3)))
        for i in range(-3,3):
            for j in range(-3,3):
                self.assertFalse(the_ref.is_winning((i,j)))

if __name__ == '__main__':
    unittest.main()






