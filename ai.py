import random

from minimax import best_move
from mcts import mcts


# =====================================
# LEVEL NAMES
# =====================================

LEVEL_NAMES = {
    1: "Very Easy",
    2: "Easy",
    3: "Medium",
    4: "Hard",
    5: "Impossible (Minimax)",
    6: "MCTS AI"
}


# =====================================
# RANDOM MOVE
# =====================================

def random_move(board):

    moves = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] == 0
    ]

    return random.choice(moves)


# =====================================
# BEST MOVE SELECTOR
# =====================================

def get_ai_move(board, difficulty):

    # LEVEL 1: Random AI
    if difficulty == 1:
        return random_move(board)

    # LEVEL 2: Mostly random
    elif difficulty == 2:
        if random.random() < 0.8:
            return random_move(board)
        return best_move(board)

    # LEVEL 3: Balanced
    elif difficulty == 3:
        if random.random() < 0.5:
            return random_move(board)
        return best_move(board)

    # LEVEL 4: Strong AI
    elif difficulty == 4:
        if random.random() < 0.2:
            return random_move(board)
        return best_move(board)

    # LEVEL 5: Perfect AI (Minimax)
    elif difficulty == 5:
        return best_move(board)

    # LEVEL 6: MCTS AI
    elif difficulty == 6:
        return mcts(board, player=-1, iterations=500)

    # fallback
    return best_move(board)