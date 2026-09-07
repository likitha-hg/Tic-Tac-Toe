Tic Tac Toe AI — Minimax

An intelligent Human vs AI Tic Tac Toe game built with Python, Pygame, NumPy, and the Minimax algorithm .

The AI evaluates possible future game states and selects the optimal move, making it impossible for the AI to lose when playing optimally. The project also includes score tracking, automatic match restart, and winner-based starting-player logic.


## Project Overview

This project demonstrates how a classical Artificial Intelligence search algorithm** can be applied to a simple but complete game environment.

Instead of using a trained machine learning model, the AI uses the Minimax algorithm to explore possible moves and determine the best action based on future game outcomes.

### Key Features

* Human vs AI gameplay
* Minimax-based AI decision making
* Complete game-tree search for 3×3 Tic Tac Toe
* AI cannot lose when playing optimally
* Human and AI score tracking
* Draw detection
* Winner detection
* Automatic match restart
* Winner gets the first move in the next match
* Draw preserves the current starting player
* Clean Pygame-based graphical interface
* Modular project structure

---

## Demo

### Gameplay

The player competes against an AI opponent powered by the Minimax algorithm.

Human: X
AI: O

The AI analyzes the available moves before selecting its next action.

> Add your gameplay screenshot or GIF here after uploading it to the repository.


Human (X)  vs  AI (O)

       |       |
    X  |   O   |
_______|_______|_______
       |       |
       |   X   |
_______|_______|_______
       |       |
       |       |


## How the AI Works

The project uses the Minimax algorithm, a classical decision-making algorithm commonly used in turn-based games.

The algorithm recursively evaluates possible future game states and assigns scores based on the outcome.

### Evaluation

The AI attempts to maximize its score while assuming that the human player will make the best possible move to minimize the AI's score.

The scoring logic is:

| Game Outcome |    Score |
| ------------ | -------: |
| AI Wins      | Positive |
| Human Wins   | Negative |
| Draw         |        0 |

The algorithm also considers the depth of the game tree so that:

* The AI prefers winning as quickly as possible.
* The AI delays losing for as long as possible.
* Draws are preferred over losing positions.

### Simplified Decision Process


Current Board
      |
      v
Find Available Moves
      |
      v
Simulate Each Move
      |
      v
Explore Future Game States
      |
      v
Evaluate Win / Loss / Draw
      |
      v
Choose Best Move
      |
      v
AI Makes Move


Because a 3×3 Tic Tac Toe game has a very small state space, the AI can search the complete game tree without requiring model training.

---

## Why Minimax?

Tic Tac Toe is a deterministic, turn-based game with a relatively small number of possible states.

For this type of problem, Minimax is an appropriate AI technique because it provides:

* Deterministic decision making
* Optimal gameplay
* No training dataset required
* No model training required
* Complete game-state evaluation
* Explainable decision making

This makes the project a practical demonstration of classical AI and adversarial search.

---

## Game Logic

The game supports the following behavior:

### Starting Player

The first game starts with the human player.

After each match:

* Human wins → Human starts the next match**
* AI wins → AI starts the next match**
* Draw → Same player starts the next match**

This creates a continuous match-based gameplay system rather than resetting the starting player after every game.

### Game States

The game recognizes three possible outcomes:


Human Wins
     |
     └── Update Human Score
             |
             └── Human starts next match


AI Wins
     |
     └── Update AI Score
             |
             └── AI starts next match


Draw
     |
     └── Update Draw Count
             |
             └── Same starter continues


---

## Technologies Used

Programming Language : Python

### Libraries

* Pygame — graphical interface and game loop
* NumPy — board representation and board-state operations

### Artificial Intelligence

* Minimax Algorithm**
* Adversarial Search
* Recursive Game-Tree Search

---

## Project Structure

```text
tic_tac_toe_ai/
│
├── main.py
│
├── minimax.py
│
├── settings.py
│
└── README.md
```

### `main.py`

Responsible for:

* Initializing Pygame
* Managing the game loop
* Handling mouse input
* Rendering the board
* Managing turns
* Calling the AI
* Detecting winners
* Detecting draws
* Maintaining scores
* Managing automatic match restart

### `minimax.py`

Contains the AI decision-making logic:

* Winner detection
* Draw detection
* Available-move generation
* Minimax recursive search
* Optimal move selection

### `settings.py`

Contains centralized configuration such as:

* Screen dimensions
* Grid dimensions
* FPS
* Cell size
* Colors
* Line width

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/tic-tac-toe-minimax-ai.git
```

### 2. Navigate to the Project

```bash
cd tic-tac-toe-minimax-ai
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install pygame numpy
```

---

## Running the Game

Run:

```bash
python main.py
```

The Pygame window will open and you can start playing against the AI.

---

## Controls

| Action              | Control                         |
| ------------------- | ------------------------------- |
| Place X             | Left mouse click                |
| Restart / New Match | Automatic after game completion |
| Quit                | Close the Pygame window         |

---

## AI Decision-Making Example

Suppose the board is:

      X | O | X
      ---------
        | O |
      ---------
      X |   |

The AI evaluates the available positions and determines which move produces the strongest possible outcome.

Rather than simply reacting to the current board, Minimax considers the consequences of each possible move.

```text
Possible Move
      |
      v
Simulate AI Move
      |
      v
Simulate Human Response
      |
      v
Simulate AI Response
      |
      v
Continue Until Terminal State
      |
      v
Evaluate Outcome
```

The best-scoring move is then selected.

---

## Algorithm

### Minimax Pseudocode

```text
MINIMAX(board, depth, maximizingPlayer)

    if AI wins:
        return positive score

    if Human wins:
        return negative score

    if board is full:
        return 0

    if maximizingPlayer:

        bestScore = -infinity

        for each available move:

            make AI move

            score = MINIMAX(
                board,
                depth + 1,
                false
            )

            undo move

            bestScore = max(bestScore, score)

        return bestScore

    else:

        bestScore = +infinity

        for each available move:

            make Human move

            score = MINIMAX(
                board,
                depth + 1,
                true
            )

            undo move

            bestScore = min(bestScore, score)

        return bestScore
```

---

## Complexity

For a standard 3×3 Tic Tac Toe board, the complete game tree is small enough to search directly.

The theoretical branching factor decreases as the board fills:

```text
9 possible moves
       ↓
8 possible moves
       ↓
7 possible moves
       ↓
...
       ↓
1 possible move
```

Because of the small state space, exhaustive Minimax search is practical for this game and produces an optimal AI without requiring machine learning.

---

## AI vs Machine Learning

This project intentionally uses **classical AI rather than machine learning**.

| Minimax AI                 | Machine Learning                |
| -------------------------- | ------------------------------- |
| No training required       | Requires training               |
| Rule/search based          | Data/model based                |
| Deterministic              | Can be probabilistic            |
| Fully explainable          | Often less transparent          |
| Searches future states     | Learns patterns/policies        |
| Ideal for small game trees | Useful for complex environments |

For Tic Tac Toe, Minimax is more suitable than training a neural network because the complete game space is small and the optimal strategy can be calculated directly.

---

## What This Project Demonstrates

This project demonstrates practical understanding of:

* Artificial Intelligence
* Adversarial Search
* Minimax
* Recursive Algorithms
* Game-State Evaluation
* Decision Making
* Python Programming
* Object/Game Logic
* Pygame Development
* NumPy
* Algorithmic Problem Solving

---

## Learning Outcome

The main goal of this project was to understand how an AI agent can make decisions by evaluating future states rather than simply reacting to the current state.

Implementing Minimax from scratch provided practical experience with:

1. Representing a game as a state space
2. Generating possible actions
3. Simulating future states
4. Recursively evaluating decisions
5. Comparing competing strategies
6. Selecting an optimal action
