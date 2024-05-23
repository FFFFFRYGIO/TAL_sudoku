import unittest

from Sudoku import get_random_sudoku, GOOD_SOLUTION
from exact_algorithm import ExactAlgorithm


class ExactAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.good_solution = GOOD_SOLUTION.copy()

    def test_exact_algorithm(self):
        sudoku = get_random_sudoku(8, self.good_solution)

        exact_algorithm = ExactAlgorithm(sudoku)

        result_sudoku = exact_algorithm.exact_algorithm()

        self.assertEqual(sudoku.count_mistakes(), 0)


if __name__ == '__main__':
    unittest.main()
