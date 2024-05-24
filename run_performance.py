import time

from Sudoku import get_random_sudoku
from good_solution_source import get_solutions
from genetic_algorithm import GeneticAlgorithm
from exact_algorithm import ExactAlgorithm


class PerformanceRunner:
    def __init__(self, num_of_empty_cells_range, genetic_algorithm_population_numbers):
        self.num_of_empty_cells_range = num_of_empty_cells_range
        self.genetic_algorithm_population_numbers = genetic_algorithm_population_numbers
        self.good_solutions = get_solutions()

    @staticmethod
    def run_exact_algorithm_performance(good_solution, num_of_empty_cells):
        print(f"Running ExactAlgorithm for num_of_empty_cells {num_of_empty_cells}")
        start_time = time.time()

        sudoku = get_random_sudoku(num_of_empty_cells, good_solution)
        exact_algorithm = ExactAlgorithm(sudoku)
        result_sudoku = exact_algorithm.exact_algorithm()

        end_time = time.time()
        elapsed_time = end_time - start_time

        if not result_sudoku.is_valid():
            raise ValueError("ExactAlgorithm: Sudoku not solved properly")

        print(f"Finished ExactAlgorithm for num_of_empty_cells {num_of_empty_cells} with time {elapsed_time}")

    @staticmethod
    def run_genetic_algorithm_performance(good_solution, num_of_empty_cells, population_number):
        print(f"Running GeneticAlgorithm for num_of_empty_cells {num_of_empty_cells} and population_number {population_number}")
        start_time = time.time()

        sudoku = get_random_sudoku(num_of_empty_cells, good_solution)
        genetic_algorithm = GeneticAlgorithm(sudoku, population_number=population_number)
        result_sudoku = genetic_algorithm.genetic_algorithm()

        if not result_sudoku.is_valid():
            raise ValueError(f"GeneticAlgorithm {population_number}: Sudoku not solved properly")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Finished GeneticAlgorithm for num_of_empty_cells {num_of_empty_cells} and population_number {population_number} with time {elapsed_time}")

    def run_for_solution(self, good_solution):
        for num_of_empty_cells in self.num_of_empty_cells_range:
            print(f"Running for num_of_empty_cells {num_of_empty_cells}")
            self.run_exact_algorithm_performance(good_solution, num_of_empty_cells)
            for population_number in self.genetic_algorithm_population_numbers:
                self.run_genetic_algorithm_performance(good_solution, num_of_empty_cells, population_number=population_number)
            print(f"Finished for num_of_empty_cells {num_of_empty_cells}")

    def main(self):
        for i, good_solution in enumerate(self.good_solutions):
            print(f"Running for good_solution {i+1}")
            self.run_for_solution(good_solution)
            print(f"Finished for good_solution {i + 1}")


if __name__ == '__main__':
    GENETIC_ALGORYTHM_POPULATION_NUMBERS = [5, 10, 20]
    NUM_OF_EMPTY_CELLS_RANGE = range(1, 7)
    runner = PerformanceRunner(NUM_OF_EMPTY_CELLS_RANGE, GENETIC_ALGORYTHM_POPULATION_NUMBERS)
    runner.main()
