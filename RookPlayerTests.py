import unittest
from rookboard import RookBoard
from rookplayer import RookPlayer

class RookPlayerTest(unittest.TestCase):

    def test_dictionary_strategy(self):
        strategy_dict_1 = {(0, 0): ("D", 1), (0, 1): ("R", 1), (1, 0): ("D", 1), (1, 1): ("R", 1), (2, 0): ("D", 2),
                           (0, 2): ("R", 2),
                           (2, 1): ("D", 1), (1, 2): ("R", 1)}
        Alice = RookPlayer(name="Alice", strategy=strategy_dict_1)
        self.assertEqual(Alice.move((0,0)), ("D",1))

    def test_function_strategy(self):
        def strategy_fun(rook_state):
            x, y = rook_state
            if x > y:
                return ("D", 1)
            else:
                return ("R", 1)

        Bob = RookPlayer(name="Bob", strategy=strategy_fun)
        self.assertEqual(Bob.move((0,0)), ("R",1))

if __name__ == '__main__':
    unittest.main()






