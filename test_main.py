# every test consists of 3 parts:
# Arrange, act, assert
import unittest

from main import TicTacToe

class TestTicTacToe(unittest.TestCase):
    mock_input = None

    def setUp(self):
        self.test_object = TicTacToe()

    def mock_take_player_input(self):
        return 0, 0

    def player_input_generator(self):
        yield 0, 0
        yield 1, 0
        yield 0, 1
        yield 1, 1
        yield 0, 2
        yield 1, 2

    def mock_player_input_generator(self):
        return next(self.mock_input)

    def test__init(self):
        self.assertEqual([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], self.test_object.board)
        self.assertEqual("X", self.test_object.active_player)

    def test__change_player(self):
        self.test_object.change_player()
        self.assertEqual("O", self.test_object.active_player)

    def test__place_piece(self):
        self.test_object.take_player_input = self.mock_take_player_input
        self.test_object.place_piece()
        self.assertEqual([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], self.test_object.board)

    def test__play_game(self):
        self.mock_input = self.player_input_generator()
        self.test_object.take_player_input = self.mock_player_input_generator
        actual_output = self.test_object.play_game()
        self.assertEqual("X wins!", actual_output)

    def tearDown(self):
        self.test_object = None

if __name__ == '__main__':
    unittest.main()