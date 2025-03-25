from termcolor import colored

class TicTacToe:
    def __init__(self):
        # Initialize the game board and winning combinations
        self.board = list(range(1, 10))  # Board positions 1-9
        self.winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), 
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                        (0, 4, 8), (2, 4, 6))  # Winning combinations
        self.moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))  # Possible moves
        self.player, self.computer = "X", "O"  # Player and computer symbols

    def print_board(self):
        # Print the current state of the board
        j = 1
        for i in self.board:
            end = " "
            if j % 3 == 0:
                end = "\n\n"  # New line after every third element
            if i == "X":
                print(colored(f"[{i}]", "red"), end=end)  # Color player X in red
            elif i == "O":
                print(colored(f"[{i}]", "blue"), end=end)  # Color player O in blue
            else:
                print(f"[{i}]", end=end)  # Print available positions
            j += 1

    def make_move(self, plyr, mve, undo=False):
        # Make a move for the player or computer
        if self.can_move(mve):
            self.board[mve - 1] = plyr  # Update board with player's move
            win = self.is_winner(plyr)  # Check if the player has won
            if undo:
                self.board[mve - 1] = mve  # Undo the move if specified
            return True, win
        return False, False  # Invalid move

    def can_move(self, mve):
        # Check if a move is valid
        return mve in range(1, 10) and isinstance(self.board[mve - 1], int)

    def is_winner(self, plyr):
        # Check if the player has won
        return any(all(self.board[j] == plyr for j in tup) for tup in self.winners)

    def has_empty_space(self):
        # Check if there are empty spaces on the board
        return self.board.count("X") + self.board.count("O") != 9

    def computer_move(self):
        # Determine the computer's move
        mv = -1
        for i in range(1, 10):
            if self.make_move(self.computer, i, True)[1]:  # Check for winning move
                mv = i
                break

        if mv == -1:
            for j in range(1, 10):
                if self.make_move(self.player, j, True)[1]:  # Block player's winning move
                    mv = j
                    break
        if mv == -1:
            for tup in self.moves:
                for m in tup:
                    if mv == -1 and self.can_move(m):  # Choose a strategic move
                        mv = m
                        break
        return self.make_move(self.computer, mv)  # Make the computer's move

    def play(self):
        # Main game loop
        print("Player: X\nComputer: O\n")
        while self.has_empty_space():
            self.print_board()  # Display the board
            move = int(input("Choose your move(1-9):"))  # Player input
            moved, won = self.make_move(self.player, move)  # Make player's move
            if not moved:
                print("Invalid Number! try again.")  # Handle invalid input
                continue
            if won:
                print(colored("You Won!", "green"))  # Player wins
                break
            elif self.computer_move()[1]:
                print(colored("You lose!", "yellow"))  # Computer wins
        self.print_board()  # Final board display

if __name__ == "__main__":
    game = TicTacToe()  # Create a new game instance
    game.play()  # Start the game
