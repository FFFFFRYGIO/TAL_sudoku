import unittest
from itertools import product

from ddt import ddt, data, unpack

from Sudoku import get_random_sudoku
from genetic_algorithm import GeneticAlgorithm
from source_manager import get_good_solution


@ddt
class GeneticAlgorithmTests(unittest.TestCase):
    def setUp(self):
        """ setUp GeneticAlgorithmTests """

        self.good_solution = get_good_solution()

    @data(*product(range(1, 5), [5, 10, 20]))
    @unpack
    def test_genetic_algorithm(self, num_of_empty_cells=5, population_number=10):
        sudoku = get_random_sudoku(num_of_empty_cells, self.good_solution)

        genetic_algorithm = GeneticAlgorithm(sudoku, population_number=population_number)

        result_sudoku = genetic_algorithm.genetic_algorithm()

        self.assertEqual(result_sudoku.count_mistakes(), 0)


if __name__ == '__main__':
    unittest.main()
