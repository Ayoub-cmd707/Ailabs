from abc import ABC
import chess
from project.chess_utilities.utility import Utility
import time
import random
"""A generic agent class"""


class Agent(ABC):

    def __init__(self, utility: Utility, time_limit_move: float) -> None:
        """Setup the Search Agent"""
        super().__init__(utility, time_limit_move)

        self.utility = utility
        self.time_limit_move = time_limit_move

    def calculate_move(self, board: chess.Board):
        start_time = time.time()

        # If the agent is playing as black, the utility values are flipped (negative-positive)
        flip_value = 1 if board.turn == chess.WHITE else -1

        best_move = random.sample(list(board.legal_moves), 1)[0]
        best_utility = 0
        # Loop trough all legal moves
        for move in list(board.legal_moves):
            # Check if the maximum calculation time for this move has been reached
            if time.time() - start_time > self.time_limit_move:
                break
            # Play the move
            board.push(move)
            # Determine the value of the board after this move
            value = flip_value * self.utility.board_value(board)
            # If this is better than all other previous moves, store this move and its utility
            if value > best_utility:
                best_move = move
                best_utility = value
            # Revert the board to its original state
            board.pop()
        return best_move
