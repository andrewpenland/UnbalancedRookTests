from genericgame import Game

from rookboard import RookBoard
from rookreferee import RookReferee
from rookplayer import RookPlayer

my_board = RookBoard((3,3))

my_referee = RookReferee(my_board)

print(my_referee.is_legal((0,0),("D",1)))


strategy_dict_1 = {(0,0):("D",1),(0,1):("R",1), (1,0): ("D",1), (1,1): ("R",1), (2,0): ("D",2),(0,2):("R",2),
                 (2,1): ("D",1), (1,2): ("R",1)}

def strategy_fun(rook_state):
    x,y = rook_state
    if x > y:
        return ("D",1)
    else:
        return ("R", 1)

Alice = RookPlayer(name = "Alice", strategy = strategy_dict_1)
Bob = RookPlayer(name = "Bob", strategy = strategy_fun)

my_players = [Alice,Bob]

my_game = Game(my_referee, my_board, my_players)

winner_name = my_game.play(verbose = True)

print("THE WINNER IS "  + str(winner_name))
