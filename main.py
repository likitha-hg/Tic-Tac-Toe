import pygame
import sys
import numpy as np

from settings import *
from minimax import (
    check_winner,
    is_draw
)

from ai import (
    get_ai_move,
    LEVEL_NAMES
)

# =====================================
# INITIALIZE PYGAME
# =====================================

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Human vs AI - Difficulty Levels + MCTS")

clock = pygame.time.Clock()

# =====================================
# GAME VARIABLES
# =====================================

board = np.zeros((3, 3), dtype=int)

starting_player = 1
current_player = starting_player

winner = None
game_over = False
game_over_time = None

# =====================================
# SCOREBOARD
# =====================================

human_wins = 0
ai_wins = 0
draws = 0

# =====================================
# DIFFICULTY
# =====================================

difficulty = 3

# =====================================
# FONTS
# =====================================

font = pygame.font.SysFont(None, 120)
small_font = pygame.font.SysFont(None, 28)

# =====================================
# DRAW GRID
# =====================================

def draw_grid():

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), LINE_WIDTH)

    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), LINE_WIDTH)

# =====================================
# DRAW SYMBOLS
# =====================================

def draw_symbols():

    for row in range(3):
        for col in range(3):

            value = board[row][col]

            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2

            if value == 1:

                text = font.render("X", True, RED)
                rect = text.get_rect(center=(x, y))
                screen.blit(text, rect)

            elif value == -1:

                text = font.render("O", True, BLUE)
                rect = text.get_rect(center=(x, y))
                screen.blit(text, rect)

# =====================================
# STATUS BAR
# =====================================

def draw_status():

    pygame.draw.rect(screen, GRAY, (0, 600, WIDTH, 100))

    if winner == 1:
        status = "You Win!"
    elif winner == -1:
        status = "AI Wins!"
    elif winner == "Draw":
        status = "Draw!"
    else:
        status = "Your Turn" if current_player == 1 else "AI Thinking..."

    level_name = LEVEL_NAMES.get(difficulty, "Unknown")

    line1 = small_font.render(status, True, BLACK)
    line2 = small_font.render(
        f"You:{human_wins}  AI:{ai_wins}  Draw:{draws}",
        True,
        BLACK
    )
    line3 = small_font.render(
        f"Level: {level_name}",
        True,
        BLACK
    )
    line4 = small_font.render(
        "[1-6] Difficulty | R: Restart",
        True,
        BLACK
    )

    screen.blit(line1, (20, 602))
    screen.blit(line2, (20, 630))
    screen.blit(line3, (350, 602))
    screen.blit(line4, (350, 630))

# =====================================
# RESET GAME
# =====================================

def reset_game():

    global board, current_player, winner, game_over, game_over_time, starting_player

    board = np.zeros((3, 3), dtype=int)

    if winner == 1:
        starting_player = 1
    elif winner == -1:
        starting_player = -1

    current_player = starting_player

    winner = None
    game_over = False
    game_over_time = None

# =====================================
# AI MOVE
# =====================================

def ai_move():

    global current_player, winner, game_over
    global ai_wins, draws, game_over_time

    if current_player == -1 and not game_over:

        pygame.time.delay(300)

        move = get_ai_move(board.copy(), difficulty)

        if move is not None:
            row, col = move
            board[row][col] = -1

        if check_winner(board, -1):

            winner = -1
            ai_wins += 1
            game_over = True
            game_over_time = pygame.time.get_ticks()
            return

        if is_draw(board):

            winner = "Draw"
            draws += 1
            game_over = True
            game_over_time = pygame.time.get_ticks()
            return

        current_player = 1

# =====================================
# MAIN LOOP
# =====================================

while True:

    clock.tick(FPS)

    draw_grid()
    draw_symbols()
    draw_status()

    pygame.display.update()

    ai_move()

    if game_over:

        current_time = pygame.time.get_ticks()

        if game_over_time and current_time - game_over_time > 2000:
            reset_game()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if current_player == 1 and not game_over:

                x, y = pygame.mouse.get_pos()

                if y < 600:

                    row = y // CELL_SIZE
                    col = x // CELL_SIZE

                    if board[row][col] == 0:

                        board[row][col] = 1

                        if check_winner(board, 1):

                            winner = 1
                            human_wins += 1
                            game_over = True
                            game_over_time = pygame.time.get_ticks()

                        elif is_draw(board):

                            winner = "Draw"
                            draws += 1
                            game_over = True
                            game_over_time = pygame.time.get_ticks()

                        else:
                            current_player = -1

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                reset_game()

            elif event.key == pygame.K_1:
                difficulty = 1

            elif event.key == pygame.K_2:
                difficulty = 2

            elif event.key == pygame.K_3:
                difficulty = 3

            elif event.key == pygame.K_4:
                difficulty = 4

            elif event.key == pygame.K_5:
                difficulty = 5

            elif event.key == pygame.K_6:
                difficulty = 6