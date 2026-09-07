import gymnasium as gym
from gymnasium import spaces
import numpy as np


class TicTacToeSelfPlayEnv(gym.Env):

    def __init__(self):

        super().__init__()

        self.board = np.zeros(
            (3, 3),
            dtype=np.int8
        )

        self.current_player = 1

        self.done = False

        self.action_space = spaces.Discrete(9)

        self.observation_space = spaces.Box(
            low=-1,
            high=1,
            shape=(3, 3),
            dtype=np.int8
        )

    # =====================================
    # OBSERVATION
    # =====================================

    def get_observation(self):

        return (
            self.board *
            self.current_player
        ).astype(np.int8)

    # =====================================
    # ACTION MASKS
    # =====================================

    def action_masks(self):

        mask = []

        for action in range(9):

            row = action // 3
            col = action % 3

            mask.append(
                self.board[row][col] == 0
            )

        return np.array(mask)

    # =====================================
    # RESET
    # =====================================

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.board = np.zeros(
            (3, 3),
            dtype=np.int8
        )

        self.current_player = 1

        self.done = False

        # ==============================
        # RANDOM START STATES
        # ==============================

        if np.random.random() < 0.30:

            num_moves = np.random.randint(
                1,
                4
            )

            for _ in range(num_moves):

                valid = np.argwhere(
                    self.board == 0
                )

                if len(valid) == 0:

                    break

                idx = np.random.randint(
                    len(valid)
                )

                row, col = valid[idx]

                self.board[row][col] = (
                    self.current_player
                )

                if self.check_winner(
                    self.current_player
                ):

                    self.board = np.zeros(
                        (3, 3),
                        dtype=np.int8
                    )

                    self.current_player = 1

                    break

                self.current_player *= -1

        return (
            self.get_observation(),
            {}
        )

    # =====================================
    # STEP
    # =====================================

    def step(self, action):

        if self.done:

            return (
                self.get_observation(),
                0,
                True,
                False,
                {}
            )

        row = action // 3
        col = action % 3

        # =================================
        # ILLEGAL MOVE
        # =================================

        if self.board[row][col] != 0:

            self.done = True

            return (
                self.get_observation(),
                -10,
                True,
                False,
                {}
            )

        reward = 0

        # =================================
        # CENTER BONUS
        # =================================

        if row == 1 and col == 1:

            reward += 0.2

        # =================================
        # PLACE MOVE
        # =================================

        self.board[row][col] = (
            self.current_player
        )

        # =================================
        # WIN
        # =================================

        if self.check_winner(
            self.current_player
        ):

            self.done = True

            reward += 10

            return (
                self.get_observation(),
                reward,
                True,
                False,
                {}
            )

        # =================================
        # DRAW
        # =================================

        if self.is_draw():

            self.done = True

            reward += 1

            return (
                self.get_observation(),
                reward,
                True,
                False,
                {}
            )

        # =================================
        # TWO-IN-A-ROW BONUS
        # =================================

        reward += self.two_in_row_bonus(
            self.current_player
        )

        # =================================
        # SWITCH PLAYER
        # =================================

        self.current_player *= -1

        return (
            self.get_observation(),
            reward,
            False,
            False,
            {}
        )

    # =====================================
    # TWO IN ROW BONUS
    # =====================================

    def two_in_row_bonus(
        self,
        player
    ):

        bonus = 0

        # Rows

        for row in range(3):

            line = self.board[row]

            if (
                np.sum(line == player) == 2
                and
                np.sum(line == 0) == 1
            ):

                bonus += 0.1

        # Columns

        for col in range(3):

            line = self.board[:, col]

            if (
                np.sum(line == player) == 2
                and
                np.sum(line == 0) == 1
            ):

                bonus += 0.1

        # Main diagonal

        diag = np.diag(self.board)

        if (
            np.sum(diag == player) == 2
            and
            np.sum(diag == 0) == 1
        ):

            bonus += 0.1

        # Anti diagonal

        diag = np.diag(
            np.fliplr(self.board)
        )

        if (
            np.sum(diag == player) == 2
            and
            np.sum(diag == 0) == 1
        ):

            bonus += 0.1

        return bonus

    # =====================================
    # WIN CHECK
    # =====================================

    def check_winner(
        self,
        player
    ):

        # Rows

        for row in range(3):

            if np.all(
                self.board[row]
                ==
                player
            ):

                return True

        # Columns

        for col in range(3):

            if np.all(
                self.board[:, col]
                ==
                player
            ):

                return True

        # Main diagonal

        if np.all(
            np.diag(self.board)
            ==
            player
        ):

            return True

        # Anti diagonal

        if np.all(
            np.diag(
                np.fliplr(
                    self.board
                )
            )
            ==
            player
        ):

            return True

        return False

    # =====================================
    # DRAW
    # =====================================

    def is_draw(self):

        return np.all(
            self.board != 0
        )

    # =====================================
    # RENDER
    # =====================================

    def render(self):

        print("\nBoard:\n")

        print(self.board)

        print(
            f"\nCurrent Player: {self.current_player}\n"
        )