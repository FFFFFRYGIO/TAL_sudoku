import unittest

from Sudoku import get_random_sudoku
from genetic_algorithm import GenericAlgorithm
from good_solution_source import get_good_solution

class ExactAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.good_solution = get_good_solution()

    def test_genetic_algorithm(self):
        sudoku = get_random_sudoku(5, self.good_solution)

        genetic_algorithm = GenericAlgorithm(sudoku, number_of_population=10)

        result_sudoku = genetic_algorithm.genetic_algorithm()

        self.assertEqual(result_sudoku.count_mistakes(), 0)


if __name__ == '__main__':
    unittest.main()
