# Class responsible for handling the board functionality
class Board:

    # initialize the board
    def __init__(self, board=[" " for i in range(9)], row=-1):
        self.board = board
        self.winner = "Game Still Up"
        self.row = row

    # fetch all possible moves for current board
    def possible_moves(self, move):
        moves = []

        # loop through all elements within the board to build new boards
        for i in range(len(self.board)):
            # if the box is blink then create new child by adding the move to it
            if self.board[i] == " ":
                # swapping single variable better than creating new array
                self.board[i] = move
                # add the new array to the possible moves
                moves.append(Board(self.board[:], i))
                self.board[i] = " "
        return moves

    # check if it's a terminate state
    def terminate_state(self):

        # Check all possible ways leads to winning game or draw
        # First row
        if self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] is not " ":
            self.update_winning_state(self.board[0])
            return True

        # Second row
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[3] != " ":
            self.update_winning_state(self.board[3])
            return True

        # Third row
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != " ":
            self.update_winning_state(self.board[6])
            return True

        # First column
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] != " ":
            self.update_winning_state(self.board[0])
            return True

        # Second column
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != " ":
            self.update_winning_state(self.board[0])
            return True

        # Third column
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != " ":
            self.update_winning_state(self.board[0])
            return True

        # First cross
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != " ":
            self.update_winning_state(self.board[0])
            return True

        # Second cross
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[2] != " ":
            self.update_winning_state(self.board[2])
            return True

        # Draw
        elif " " not in self.board:
            self.winner = 0
            return True

        # Game is still up
        else:
            return False

    # Update the value of the board if it's a terminate
    def update_winning_state(self, winner):
        if winner == "X":
            self.winner = 10
        else:
            self.winner = -10

    # draw the board
    def draw(self):
        for j in range(8):
            print "_",
        print ""
        index = 0
        for i in range(3):
            for j in self.board[index:index+3]:
                print "| {} ".format(j),
            print "|"
            for j in range(8):
                print "_",
            print ""
            index += 3
