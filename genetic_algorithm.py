import copy
from random import randint, shuffle, choice

from Sudoku import Sudoku


class GeneticAlgorithm:
    def __init__(self, sudoku_to_solve: Sudoku, population_number: int = 10):
        self.sudoku_to_solve = copy.deepcopy(sudoku_to_solve)
        self.population_number = population_number
        self.population = []

    def initial_population(self):
        """ generate first random solutions """

        for _ in range(self.population_number):
            sudoku = copy.deepcopy(self.sudoku_to_solve)

            for i, j in self.sudoku_to_solve.non_perm_cells_list:
                sudoku.board[i][j] = randint(1, 9)

            self.population.append(sudoku)

    def fitness_evaluation(self):
        """ generate mark for every solution """

        for i in range(len(self.population)):
            self.population[i].mark_solution()

    def selection_of_population(self):
        """ shorten population to max_population_number by removing those with bad mark """

        sorted_population = sorted(self.population, key=lambda sudoku: sudoku.mark)
        trimmed_population = sorted_population[:self.population_number]
        self.population = trimmed_population

    def crossover_population(self):
        """ create child solutions based on 2 currently existing solutions """

        shuffle(self.population)
        for first_parent_index in range(0, len(self.population) - 1, 2):
            parent1 = self.population[first_parent_index]
            parent2 = self.population[first_parent_index + 1]
            child = copy.deepcopy(self.sudoku_to_solve)
            which_parent = 1
            for i, j in self.sudoku_to_solve.non_perm_cells_list:
                if which_parent == 1:
                    child.board[i][j] = parent1.board[i][j]
                    which_parent += 1
                else:
                    child.board[i][j] = parent2.board[i][j]
                    which_parent -= 1

            self.population.append(child)

    def mutate_population(self):
        """ create mutations for current solutions list """

        for solution in self.population:
            i, j = choice(self.sudoku_to_solve.non_perm_cells_list)
            current_value_of_cell = solution.board[i][j]
            possible_mutations = [i for i in range(1, 10) if i != current_value_of_cell]
            solution.board[i][j] = choice(possible_mutations)

    def termination_condition_check(self):
        """ check if the condition is finished and the result is here """

        for solution in self.population:
            if solution.is_valid():
                return solution
        return None

    def genetic_algorithm(self) -> Sudoku:
        # 1. Initial Population
        self.initial_population()

        result = None
        while not result:
            # 2. Fitness Evaluation
            self.fitness_evaluation()
            # 3. Selection of population
            self.selection_of_population()
            # 4. Crossover population
            self.crossover_population()
            # 5. Mutation
            self.mutate_population()
            # 6. Replacement
            # already done during the program
            # 7. Termination Condition check
            result = self.termination_condition_check()

        # 8. Result Extraction
        return result
