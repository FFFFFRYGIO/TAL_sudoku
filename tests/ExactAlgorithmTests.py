import unittest

from Sudoku import get_random_sudoku
from exact_algorithm import ExactAlgorithm
from source_manager import get_good_solution


class ExactAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.good_solution = get_good_solution()

    def test_exact_algorithm(self):
        sudoku = get_random_sudoku(5, self.good_solution)

        exact_algorithm = ExactAlgorithm(sudoku)

        result_sudoku = exact_algorithm.exact_algorithm()

        self.assertEqual(result_sudoku.count_mistakes(), 0)


if __name__ == '__main__':
    unittest.main()
