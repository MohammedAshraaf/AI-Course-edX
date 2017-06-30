# For the State Characteristics
class State:
    # initialize the state
    def __init__(self, moves, prev_steps):
        # the configuration
        self.item = []
        # The moves to get to this configuration which extends from its parent
        self.moves = moves
        # the cost to reach this configuration which extends from its parent
        self.prevSteps = prev_steps

    # add new move to it
    def add_move(self, move):
        self.moves.append(move)

    # add the configuration
    def create_item(self, arr):
        self.item = arr
