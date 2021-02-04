import string

EMPTY_SQUARE = " "
BOARD_SIZE = 3
PIECE_ONE = "X"
PIECE_TWO = "O"


class TicTacToe:
    def __init__(self, size=BOARD_SIZE):
        """Initialise the board, and set the starting player as 'X'."""
        self.board = [[EMPTY_SQUARE for _ in range(size)] for __ in range(size)]
        self.player = PIECE_ONE

    def __str__(self):
        output_str = " " * 4
        for index in range(len(self.board[0])):
            output_str += str(index + 1) + (" " * 3)
        output_str += "\n"
        for row_index in range(len(self.board)):
            output_str += string.ascii_uppercase[row_index]
            for cell in self.board[row_index]:
                output_str += " | " + cell
            output_str += " |" + "\n"
        return output_str

    def change_player(self):
        player = PIECE_TWO if self.player == PIECE_ONE else PIECE_ONE
        return player

    def player_input(self):
        while True:
            input_value = input("Please select a row and a column to place the" + self.player + "!").upper()
            if len(input_value) != 2:  # Input needs to be 2 characters long
                continue
            else:
                row_index = string.ascii_uppercase.find(input_value[0])  # Transform the letter into an index
                col_index = int(input_value[1]) - 1  # Transform human input to index
                if input_value[0] not in string.ascii_uppercase or not input_value[1].isdigit():  # if value not letter
                    continue
                if row_index > BOARD_SIZE - 1 or col_index > BOARD_SIZE - 1:
                    continue
            return row_index, col_index

    def place_piece(self):
        while True:  # Call input until value provided is valid for the board state
            row_index, col_index = self.player_input()
            if self.board[row_index][col_index] == EMPTY_SQUARE:
                self.board[row_index][col_index] = self.player
                break

    def get_diagonal(self, board):
        """Returns forward diagonal as a list to be added to get_all_lines()"""
        diagonal = []
        for index in range(len(board)):
            diagonal.append(board[index][index])
        return diagonal

    def get_all_lines(self):
        """Returns all rows, columns, and diagonals to be checked by win_con()"""
        all_lines = []
        for row in self.board:
            all_lines.append(row)
        for col_index in range(len(self.board)):
            column = []
            for row_index in range(len(self.board)):
                column.append(self.board[row_index][col_index])
            all_lines.append(column)
        all_lines.append(self.get_diagonal(self.board))
        all_lines.append(self.get_diagonal(self.board[::-1]))
        return all_lines

    def win_con(self, lines):
        for line in lines:
            if line.count(self.player) == 3:
                print(self.__str__())
                print(self.player + " wins!")
                return True

    def board_full(self):
        for row in game_board.board:
            if row.count(EMPTY_SQUARE) != 0:
                return False
        print(self.__str__())
        print("Draw!")
        return True

    def game_loop(self):
        while True:
            print(self.__str__())
            self.place_piece()
            if self.win_con(self.get_all_lines()):
                return True
            if self.board_full():
                return True
            self.player = self.change_player()


if __name__ == "__main__" == __name__:
    game_board = TicTacToe()
    game_board.game_loop()
