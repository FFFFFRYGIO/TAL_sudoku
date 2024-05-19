import unittest

from Sudoku import INIT_CELLS, Sudoku
from exact_algorithm import ExactAlgorithm


class ExactAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.init_cells = INIT_CELLS

    def test_exact_algorithm(self):
        sudoku = Sudoku(self.init_cells)

        exact_algorithm = ExactAlgorithm(sudoku)

        result = exact_algorithm.exact_algorithm()

        assert exact_algorithm.sudoku.count_mistakes() == 0


if __name__ == '__main__':
    unittest.main()