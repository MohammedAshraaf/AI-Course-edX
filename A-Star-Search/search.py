import sys
import math
from priorityQueue import PriorityQueue
from state import State

# This A* search for 8-Puzzle game


def main():
    # check if the user entered invalid command
    if len(sys.argv) != 2:
        print "Error! usage => python search.py *configuration*"
        return
    # get the board from the command line
    game = sys.argv[1].split(',')
    # convert strings to numbers
    game = map(int, game)
    # initiate the start state
    start = State([], 0)
    start.create_item(game)
    # create the goal board
    biggest = max(game)
    goal = [i for i in range(int(biggest) + 1)]
    # create possible moves for each index based on the length and the type of the search
    moves = possible_moves(game, sys.argv[1])
    # print the result
    print a_star_search(start, goal, moves)


# searches for the goal using A*
def a_star_search(start, goal, moves):
    # Create the Frontier
    frontier = PriorityQueue()
    # add the start node to the frontier
    frontier.put(start, g_of_n(start) + h_of_n(start))
    # explore the node
    explored = explored_dic(len(start.item))
    # loop as long frontier is not input
    while frontier.not_empty():
        # get the node with the highest priority
        state = frontier.get()
        # check if it's the goal then return the moves
        if state.item == goal:
            return state.moves
        # get the index of zero for the dictionary
        zero = state.item.index(0)
        # add the node to explored using
        explored[zero].add(tuple(state.item))
        for move in moves[zero]:
            new_child = State(state.moves[:], state.prevSteps + 1)
            new_child.create_item(move_list(move, state.item[:], zero))
            zero2 = new_child.item.index(0)
            if tuple(new_child.item) in explored[zero2] or frontier.in_frontier(tuple(new_child.item)):
                continue
            else:
                # add the new move to the child
                new_child.add_move(move)
                frontier.put(new_child, g_of_n(new_child) + h_of_n(new_child))
    return "nothing"


# the cost to this current state
def g_of_n(state):
    return state.prevSteps


# Heuristic function to calculate the cost from this state to the goal state
def h_of_n(state):
    cost = 0
    length = len(state.item)
    # for each value within the board
    # calculate the distance between the current position and the correct position
    for i in state.item:
        cost += (abs(i - state.item.index(i)) / length) + (abs(i - state.item.index(i)) % length)
    return cost


# prepares the possible moves for each index within the board
def possible_moves(search_list, method):
    moves = list()
    n = math.sqrt(len(search_list))
    for i in range(len(search_list)):
        directions = list()
        if i < n:
            directions.append('D')
        elif i >= len(search_list) - n:
            directions.append('U')
        else:
            directions.append('U')
            directions.append('D')
        if i % n == 0:
            directions.append('R')
        elif i % n == n - 1:
            directions.append('L')
        else:
            directions.append('L')
            directions.append('R')
        if method == 'dfs':
            directions.reverse()
        moves.append(directions)
    return moves


# create new configuration from a list by moving the space
def move_list(move, state, zero):
    n = int(math.sqrt(len(state)))
    if move == 'U':
        state[zero], state[zero - n] = state[zero - n], state[zero]
    elif move == 'D':
        state[zero], state[zero + n] = state[zero + n], state[zero]
    elif move == 'L':
        state[zero], state[zero - 1] = state[zero - 1], state[zero]
    else:
        state[zero], state[zero + 1] = state[zero + 1], state[zero]
    return state


# create dictionary full of sets for the explored data structure to optimize the search process
def explored_dic(length):
    dic = {i: set() for i in range(length)}
    return dic


if __name__ == '__main__':
    main()
