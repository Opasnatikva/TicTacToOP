EMPTY_SQUARE = " "
BOARD_SIZE = 3


class TicTacToe:

    def __init__(self, size=BOARD_SIZE):
        self.board = []
        for row in range(size):
            for col in range(size):
                self.board.append(EMPTY_SQUARE)

    def __str__(self):
        output_str = ""
        for row in self.board:
            output_str += "|" + str(row) + "|" + "\n"
        return output_str


if __name__ == "__main__":
    game_board = TicTacToe()
    print(game_board)