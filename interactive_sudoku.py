import time

from Sudoku import Sudoku
from exact_algorithm import ExactAlgorithm
from genetic_algorithm import GeneticAlgorithm
from source_manager import get_problem

if __name__ == '__main__':
    sudoku_problem_file = input('Please enter a file name with sudoku problem: ')  # sudoku_problem.txt

    genetic_population_number = None
    while not isinstance(genetic_population_number, int):
        try:
            genetic_population_number = int(input('Please enter a population number for genetic algorithm: '))  # 10
        except ValueError:
            print('Please input a number')

    sudoku_problem = get_problem(sudoku_problem_file)
    sudoku = Sudoku(sudoku_problem)

    print("Solving with genetic algorithm")
    genetic_algorithm = GeneticAlgorithm(sudoku)

    start_time = time.time()

    result = genetic_algorithm.genetic_algorithm()

    end_time = time.time()
    elapsed_time = end_time - start_time

    if not result.is_valid():
        raise Exception("Genetic algorithm result is not valid")
    print(f'Solved with genetic algorithm with time {elapsed_time}')

    print("Solving with exact algorithm")
    exact_algorithm = ExactAlgorithm(sudoku)

    start_time = time.time()

    result = exact_algorithm.exact_algorithm()

    end_time = time.time()
    elapsed_time = end_time - start_time

    if not result.is_valid():
        raise Exception("Exact algorithm result is not valid")
    print(f'Solved with exact algorithm with time {elapsed_time}')
