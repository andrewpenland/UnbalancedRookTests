##
# This implements a Game that takes a list/set of players, a referee, and a
# board. It automates the process of playing the game, and returns a winner.
#
# Authors: Daniel Hammer, Nicholas O'Kelley, Andrew Shelton
#
# Date: Sep 22, 2020
##

import referee
import player
import board

class Game:
    def __init__(self, the_referee, the_board, the_players):
        """The game constructor declares a new board, referee, and two
        players.

        Args:
            referee : the current game referee
            board : the game board
            first : the first player

        """
        self.game_referee = the_referee
        self.game_board = the_board
        self.game_players = the_players

    def play(self, verbose=False):
        """ This function allows for the game to be played.

        Args:
            None

        Return:
            winning_player_name, the name of the winning player
            winning_player, the type of player
            player_number (0 or 1), whether they went first or secons
        """
        current_player = self.game_players[0]
        player_number = 0
        game_over = False
        if verbose:
            title = "Name \t Move \t New Board \n"
            print(title)
            print("-" * len(title))
        while (not (game_over)):
            player_move = current_player.move(self.game_board.state)
            if self.game_referee.is_legal(self.game_board.state, player_move):
                new_state = self.game_board.update(player_move)
                if self.game_referee.is_winning(new_state):
                    winning_player_name = current_player.name
                    winning_player = current_player
                    game_over = True
                    return winning_player_name, winning_player, player_number
                else:  # the move is legal but does not win
                    self.game_board.state = new_state
                    player_number = (player_number + 1) % 2
                    current_player = self.game_players[player_number]
                    if verbose:
                        print(current_player.name + "\t" + str(player_move) + "\t" + str(new_state) + "\n")

            else:  # the move is not legal
                game_over = True
                winning_player_number = (player_number + 1) % 2
                winning_player = self.game_players[winning_player_number]
                winning_player_name = self.game_players[winning_player_number].name
                return winning_player_name, winning_player, winning_player_number




