from project.chess_agents.agent import Agent
import chess
from project.chess_utilities.utility import Utility
import time
import os
import random
import chess.polyglot

"""An example search agent with two implemented methods to determine the next move"""
class ExampleAgent(Agent):

    # Initialize your agent with whatever parameters you want
    def __init__(self, utility: Utility, time_limit_move: float) -> None:
        super().__init__(utility, time_limit_move)
        self.name = "Example search agent"
        self.author = "Aouraghe Ayoub &Tenzin Lote"
        self.time_limit_move = time_limit_move
        self.utility = utility

    # This agent does not perform any searching, it sinmply iterates trough all the moves possible and picks the one with the highest utility
    def calculate_move(self, board: chess.Board):

        flip_value = True if board.turn == chess.WHITE else False
        try:
            openingMove = chess.polyglot.MemoryMappedReader(os.path.dirname(__file__).split("\project")[0] + "\\GMopenings.bin").weighted_choice(board).move
            print("yes sir")
            return openingMove
        except:
            start_time = time.time()

            bestMove = chess.Move.null()
            bestValue = -float('inf')

            alpha = -999999999
            beta = 999999999

            for move in board.legal_moves:
                if time.time() - start_time > self.time_limit_move:
                    print("Move Bitch")
                    break
                board.push(move)
                boardValue = -self.minimaxAlphaBeta(board, 3, beta, alpha,flip_value)
                if boardValue > bestValue:
                    bestValue = boardValue;
                    bestMove = move
                if (boardValue > alpha):
                    alpha = boardValue
                board.pop()
            return bestMove

    def minimaxAlphaBeta(self,board:chess.Board, depth, alpha, beta, maximizing_player):

        if depth == 0 or board.is_game_over():
            return self.utility.board_value(board)
        if maximizing_player:
            value = -float('inf')
            for move in board.legal_moves:

                board.push(move)
                value = max(value, self.minimaxAlphaBeta(board, depth - 1, beta, alpha, False))
                board.pop()
                if (value >= beta):
                    return value
                if (value > alpha):
                    alpha = value
            return value
        else:
            value = float('inf')
            for move in board.legal_moves:

                board.push(move)
                value = min(value, self.minimaxAlphaBeta(board, depth - 1, beta, alpha, True))
                board.pop()
                if (value >= beta):
                    return value
                if (value > alpha):
                    alpha = value
            return value

