import numpy as np
import math
import random

# =====================================
# GAME UTILITIES
# =====================================

def check_winner(board, player):

    # Rows
    for r in range(3):
        if np.all(board[r, :] == player):
            return True

    # Columns
    for c in range(3):
        if np.all(board[:, c] == player):
            return True

    # Diagonals
    if np.all(np.diag(board) == player):
        return True

    if np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False


def is_draw(board):
    return not np.any(board == 0)


def get_valid_moves(board):

    return [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] == 0
    ]


# =====================================
# MCTS NODE
# =====================================

class Node:

    def __init__(self, board, player, parent=None, move=None):

        self.board = board.copy()
        self.player = player  # player to move at this node

        self.parent = parent
        self.move = move

        self.children = []

        self.visits = 0
        self.wins = 0

        self.untried_moves = get_valid_moves(board)


# =====================================
# UCB1 SCORE
# =====================================

def ucb1(node, c=1.4):

    if node.visits == 0:
        return float("inf")

    return (
        node.wins / node.visits
        + c * math.sqrt(
            math.log(node.parent.visits) / node.visits
        )
    )


# =====================================
# EXPAND NODE
# =====================================

def expand(node):

    move = node.untried_moves.pop()
    r, c = move

    new_board = node.board.copy()
    new_board[r][c] = node.player

    child = Node(
        new_board,
        -node.player,
        node,
        move
    )

    node.children.append(child)

    return child


# =====================================
# SIMULATION (RANDOM PLAYOUT)
# =====================================

def simulate(board, player):

    current_board = board.copy()
    turn = player

    while True:

        moves = get_valid_moves(current_board)

        if not moves:
            return 0

        move = random.choice(moves)
        r, c = move

        current_board[r][c] = turn

        if check_winner(current_board, turn):
            return turn

        if is_draw(current_board):
            return 0

        turn *= -1


# =====================================
# BACKPROPAGATION
# =====================================

def backpropagate(node, result):

    while node is not None:

        node.visits += 1

        # reward system
        if node.player == result:
            node.wins += 1

        node = node.parent


# =====================================
# MCTS MAIN FUNCTION
# =====================================

def mcts(root_board, player=-1, iterations=500):

    root = Node(root_board, player)

    for _ in range(iterations):

        node = root

        # -------------------------
        # SELECTION
        # -------------------------
        while node.children and not node.untried_moves:
            node = max(node.children, key=ucb1)

        # -------------------------
        # EXPANSION
        # -------------------------
        if node.untried_moves:
            node = expand(node)

        # -------------------------
        # SIMULATION
        # -------------------------
        result = simulate(node.board, node.player)

        # -------------------------
        # BACKPROPAGATION
        # -------------------------
        backpropagate(node, result)

    # =================================
    # BEST MOVE SELECTION
    # =================================

    best_child = max(root.children, key=lambda n: n.visits)

    return best_child.move