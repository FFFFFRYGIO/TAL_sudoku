import unittest
from Sudoku import Sudoku, Cell, INIT_CELLS, GOOD_SOLUTION


class SudokuTests(unittest.TestCase):
    def setUp(self):
        self.init_cells = INIT_CELLS
        self.good_solution = GOOD_SOLUTION

    def test_sudoku_good_solution(self):
        sudoku = Sudoku(self.init_cells)

        for i, j, k in self.good_solution:
            sudoku.board[i][j] = Cell(k)

        assert sudoku.count_mistakes() == 0


if __name__ == '__main__':
    unittest.main()
