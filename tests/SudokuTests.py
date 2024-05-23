import unittest

from Sudoku import Sudoku, get_random_sudoku
from good_solution_source import get_good_solution


class SudokuTests(unittest.TestCase):
    def setUp(self):
        self.good_solution = get_good_solution()

    def test_sudoku_good_solution_count_mistakes(self):
        sudoku = get_random_sudoku(10, self.good_solution)

        for i, j, value in self.good_solution:
            sudoku.board[i][j] = value

        self.assertEqual(sudoku.count_mistakes(), 0)

    def test_sudoku_good_solution_is_valid(self):
        sudoku = Sudoku(self.good_solution)

        for i, j, value in self.good_solution:
            sudoku.board[i][j] = value

        self.assertTrue(sudoku.is_valid())


if __name__ == '__main__':
    unittest.main()
