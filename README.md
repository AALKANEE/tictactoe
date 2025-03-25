# Tic-Tac-Toe Game

A simple command-line Tic-Tac-Toe game written in Python. The game allows a player to compete against the computer with strategic moves.

## Features
- Play against an AI opponent.
- Highlights winning moves.
- Color-coded board using `termcolor`.

## Requirements
Make sure you have Python installed along with the required package:
```bash
pip install termcolor
```

## How to Play
1. Run the script using:
   ```bash
   python main.py
   ```
2. The player is assigned `X` and the computer is `O`.
3. Enter a number (1-9) to place your move.
4. The game continues until either player wins or all spaces are filled.

## Example Output
```
Player: X
Computer: O

[1] [2] [3]

[4] [5] [6]

[7] [8] [9]

Choose your move (1-9):
```

## Game Logic
- The computer plays strategically by blocking the player and prioritizing winning moves.
- The game board updates dynamically after each move.

## License
This project is open-source and available for use under the MIT License.

Enjoy playing Tic-Tac-Toe! 🎮

