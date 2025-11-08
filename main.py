"""
Tic Tac Toe Game
Author: <Theo>
Date: 2023-03-26
License: Unlicensed
"""
import string

EMPTY_SQUARE = " "
BOARD_SIZE = 3
PIECE_ONE = "X"
PIECE_TWO = "O"


class TicTacToe:
    """A class to represent a Tic Tac Toe game board."""

    def __init__(self, size=BOARD_SIZE):
        """Initialise the board, and set the starting player as 'X'."""
        self.board = [[EMPTY_SQUARE for _ in range(size)] for __ in range(size)]
        self.active_player = PIECE_ONE

    def __call__(self):
        """Play the game until a winner is found or the board is full."""
        self.play_game()

    def __str__(self):
        """Return a string representation of the board."""
        output_str = " " * 4
        for index in range(BOARD_SIZE):
            output_str += str(index + 1) + (" " * 3)
        output_str += "\n"
        for row_index in range(BOARD_SIZE):
            output_str += string.ascii_uppercase[row_index]
            for cell in self.board[row_index]:
                output_str += " | " + cell
            output_str += " |" + "\n"
        return output_str

    def change_player(self):
        """Change the active player."""
        self.active_player = PIECE_TWO if self.active_player == PIECE_ONE else PIECE_ONE

    def take_player_input(self):
        """Take player input and return the row and column indices."""
        while True:
            input_value = input(
                "Please select a row and a column to place the " + \
                self.active_player + "!").upper()
            if len(input_value) != 2:  # Input needs to be 2 characters long
                continue

            if input_value[0] not in string.ascii_uppercase or not \
                    input_value[1].isdigit():  # if value not letter
                continue
            row_index = string.ascii_uppercase.find(
                input_value[0])  # Transform the letter into an index
            col_index = int(input_value[1]) - 1  # Transform human input to index
            if row_index > BOARD_SIZE - 1 or col_index > BOARD_SIZE - 1:
                continue
            return row_index, col_index

    def place_piece(self):
        """Place the active player's piece on the board."""
        while True:  # Call input until value provided is valid for the board state
            row_index, col_index = self.take_player_input()
            if self.board[row_index][col_index] == EMPTY_SQUARE:
                self.board[row_index][col_index] = self.active_player
                break

    def get_diagonal(self, board):
        """Returns forward diagonal as a list to be added to get_all_lines()"""
        diagonal = []
        for index in range(BOARD_SIZE):
            diagonal.append(board[index][index])
        return diagonal

    def get_all_lines(self):
        """Returns all rows, columns, and diagonals to be checked by win_con()"""
        all_lines = []
        for row in self.board:
            all_lines.append(row)
        for col_index in range(BOARD_SIZE):
            column = []
            for row_index in range(BOARD_SIZE):
                column.append(self.board[row_index][col_index])
            all_lines.append(column)
        all_lines.append(self.get_diagonal(self.board))
        all_lines.append(self.get_diagonal(self.board[::-1]))
        return all_lines

    def check_win_con(self, lines):
        """Checks if the active player has won the game."""
        for line in lines:
            if line.count(self.active_player) == 3:
                print(self)
                print(self.active_player + " wins!")
                return True
        return False

    def check_board_full(self):
        """Checks if the board is full."""
        for row in self.board:
            if row.count(EMPTY_SQUARE) != 0:
                return False
        print(self)
        print("Draw!")
        return True

    def play_game(self):
        """Play the game until a winner is found or the board is full."""
        while True:
            print(self)
            self.place_piece()
            if self.check_win_con(self.get_all_lines()) or self.check_board_full():
                break
            self.change_player()


if __name__ == "__main__" == __name__:
    game = TicTacToe()
    game()
