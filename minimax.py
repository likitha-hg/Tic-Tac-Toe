import numpy as np

# =====================================
# CHECK WINNER
# =====================================

def check_winner(board, player):

    # Rows
    for row in range(3):

        if np.all(board[row] == player):

            return True

    # Columns
    for col in range(3):

        if np.all(board[:, col] == player):

            return True

    # Main diagonal
    if np.all(
        np.diag(board)
        ==
        player
    ):

        return True

    # Anti diagonal
    if np.all(
        np.diag(
            np.fliplr(board)
        )
        ==
        player
    ):

        return True

    return False


# =====================================
# DRAW CHECK
# =====================================

def is_draw(board):

    return np.all(board != 0)


# =====================================
# GET AVAILABLE MOVES
# =====================================

def get_available_moves(board):

    moves = []

    for row in range(3):

        for col in range(3):

            if board[row][col] == 0:

                moves.append(
                    (row, col)
                )

    return moves


# =====================================
# MINIMAX
# =====================================

def minimax(board, depth, maximizing):

    # ==============================
    # TERMINAL STATES
    # ==============================

    # AI wins
    if check_winner(board, -1):

        return 10 - depth

    # Human wins
    if check_winner(board, 1):

        return depth - 10

    # Draw
    if is_draw(board):

        return 0

    # ==============================
    # MAXIMIZING PLAYER (AI)
    # ==============================

    if maximizing:

        best_score = -1000

        for row, col in get_available_moves(board):

            board[row][col] = -1

            score = minimax(
                board,
                depth + 1,
                False
            )

            board[row][col] = 0

            best_score = max(
                best_score,
                score
            )

        return best_score

    # ==============================
    # MINIMIZING PLAYER (HUMAN)
    # ==============================

    else:

        best_score = 1000

        for row, col in get_available_moves(board):

            board[row][col] = 1

            score = minimax(
                board,
                depth + 1,
                True
            )

            board[row][col] = 0

            best_score = min(
                best_score,
                score
            )

        return best_score


# =====================================
# BEST MOVE FOR AI
# =====================================

def best_move(board):

    best_score = -1000

    move = None

    for row, col in get_available_moves(board):

        board[row][col] = -1

        score = minimax(
            board,
            0,
            False
        )

        board[row][col] = 0

        if score > best_score:

            best_score = score

            move = (row, col)

    return move