import sys
from board import Board


# evaluate the current board and play the best move
# from the perspective of the current player
def minimax(board, max_turn, depth, alpha=-sys.maxint - 1, beta=sys.maxint):
    # if this a terminate board then return the winner
    if board.terminate_state():
        return board.winner - depth

    # max turn .. chose the best move
    if max_turn:
        best_movie = -sys.maxint - 1

        # generate all possible moves for this current board
        for child in board.possible_moves('X'):
            # call minimax recursively and give the turn to min
            move_result = minimax(child, False, depth + 1, alpha, beta)

            # if we found a better move then chose it
            best_movie = max(move_result, best_movie)

            # get the best alpha and stop if alpha greater than beta!
            alpha = max(alpha, best_movie)
            if alpha >= beta:
                break

        # return the best move
        return best_movie

    # min turn .. chose the worst move ..
    # ** the same as max but for min with minimum values **
    else:
        worst_movie = sys.maxint

        for child in board.possible_moves('O'):
            move_result = minimax(child, True, depth + 1, alpha, beta)

            worst_movie = min(move_result, worst_movie)
            beta = min(beta, worst_movie)

            if beta <= alpha:
                break
        return worst_movie
