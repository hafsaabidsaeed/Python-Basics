#importing necessary libraries

import chess
import chess.pgn            # reading and writing portable game notation
import pandas as pd         #data manipulation
from io import StringIO     # handling string as file like object

# Load Lichess Games Statistics dataset
lichess_data = pd.read_csv(r'D:\AI Lab\archive\Chess games stats.csv')     #load data

# Function to evaluate the chess board position
# assign values to different chess piece using dictionary (piece_values)
# then calculate simple score for a chess postition based on values assigned
def evaluate_position(board):
    return sum(piece_values.get(piece, 0) for piece in board.piece_map().values())

# Function to get legal moves for a board
def get_legal_moves(board):
    return list(board.legal_moves)

# Simple piece values for evaluation (can be customized)
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0  # Assume the king is not directly captured
}

# Minimax algorithm (without Alpha-Beta Pruning)
def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)

    legal_moves = get_legal_moves(board)

    if maximizing_player:
        max_eval = float("-inf")
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            max_eval = max(max_eval, eval)
            board.pop()
        return max_eval
    else:
        min_eval = float("inf")
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            min_eval = min(min_eval, eval)
            board.pop()
        return min_eval

# Function to get the best move using minimax
def get_best_move(board, depth):
    legal_moves = get_legal_moves(board)
    best_move = None
    best_eval = float("-inf")

    for move in legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, False)
        board.pop()

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move

# Example Usage
if __name__ == "__main__":
    # Convert the numeric value to a string before passing it to StringIO
    game = chess.pgn.read_game(StringIO(str(lichess_data["White Centi-pawn Loss"].iloc[0])))
    board = game.board()

    # Get the best move using minimax (without Alpha-Beta Pruning)
    best_move = get_best_move(board, depth=2)

    print("Best Move:", best_move)
