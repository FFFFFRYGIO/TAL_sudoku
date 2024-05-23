import copy
from random import randint

from Sudoku import Sudoku


class GenericAlgorithm:
    def __init__(self, sudoku_to_solve: Sudoku, number_of_population=10):
        self.sudoku_to_solve = copy.deepcopy(sudoku_to_solve)
        self.population = [self.get_random_solution() for _ in range(number_of_population)]

    def get_random_solution(self):
        """ Get random sudoku solution """
        sudoku = copy.deepcopy(self.sudoku_to_solve)

        for i, j in self.sudoku_to_solve.non_perm_cells_list:
            sudoku.board[i][j] = randint(1, 9)

    def genetic_algorithm(self):
        return self.sudoku_to_solve
