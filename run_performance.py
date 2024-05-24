import os
import time

import openpyxl
import pandas as pd
from openpyxl.chart import LineChart, Reference

from Sudoku import get_random_sudoku
from exact_algorithm import ExactAlgorithm
from genetic_algorithm import GeneticAlgorithm
from source_manager import get_solutions


class PerformanceRunner:
    def __init__(self, num_of_empty_cells_range, genetic_algorithm_population_numbers):
        self.num_of_empty_cells_range = num_of_empty_cells_range
        self.genetic_algorithm_population_numbers = genetic_algorithm_population_numbers
        self.good_solutions = get_solutions()

        self.results = {}
        for n in self.num_of_empty_cells_range:
            self.results.update({f'index_{n}': []})
            self.results.update({f'exact_{n}': []})
            self.results.update({f'genetic_{p}_{n}': [] for p in self.genetic_algorithm_population_numbers})


    @staticmethod
    def run_exact_algorithm_performance(good_solution, num_of_empty_cells):
        print(f"Running ExactAlgorithm for n={num_of_empty_cells}")
        start_time = time.time()

        sudoku = get_random_sudoku(num_of_empty_cells, good_solution)
        exact_algorithm = ExactAlgorithm(sudoku)
        result_sudoku = exact_algorithm.exact_algorithm()

        end_time = time.time()
        elapsed_time = end_time - start_time

        if not result_sudoku.is_valid():
            raise ValueError("ExactAlgorithm: Sudoku not solved properly")

        print(f"Finished ExactAlgorithm for n={num_of_empty_cells} with time {elapsed_time}")
        return elapsed_time

    @staticmethod
    def run_genetic_algorithm_performance(good_solution, num_of_empty_cells, population_number):
        print(f"Running GeneticAlgorithm for p={population_number} and n={num_of_empty_cells}")
        start_time = time.time()

        sudoku = get_random_sudoku(num_of_empty_cells, good_solution)
        genetic_algorithm = GeneticAlgorithm(sudoku, population_number=population_number)
        result_sudoku = genetic_algorithm.genetic_algorithm()

        end_time = time.time()
        elapsed_time = end_time - start_time

        if not result_sudoku.is_valid():
            raise ValueError(f"GeneticAlgorithm {population_number}: Sudoku not solved properly")

        print(f"Finished GeneticAlgorithm for p={population_number} and n={num_of_empty_cells} with time {elapsed_time}")
        return elapsed_time

    def run_for_solution(self, good_solution):
        for num_of_empty_cells in self.num_of_empty_cells_range:
            print(f"Running for n={num_of_empty_cells}")

            for _ in range(10):
                exact_time = self.run_exact_algorithm_performance(good_solution, num_of_empty_cells)
                self.results[f'exact_{num_of_empty_cells}'].append(exact_time)

            for population_number in self.genetic_algorithm_population_numbers:
                for _ in range(10):
                    genetic_time = self.run_genetic_algorithm_performance(good_solution, num_of_empty_cells, population_number)
                    self.results[f'genetic_{population_number}_{num_of_empty_cells}'].append(genetic_time)

            print(f"Finished for n={num_of_empty_cells}")

    def main(self):
        for i, good_solution in enumerate(self.good_solutions):
            print(f"Running for good_solution {i+1}")
            self.run_for_solution(good_solution)
            print(f"Finished for good_solution {i + 1}")

        df = pd.DataFrame.from_dict(self.results, orient='index').transpose()
        for n in self.num_of_empty_cells_range:
            df[f'index_{n}'] = df.index

        if not os.path.exists('performance_results'):
            os.makedirs('performance_results')

        df.to_excel(os.path.join('performance_results', 'performance_results.xlsx'), engine='openpyxl')

        wb = openpyxl.load_workbook(os.path.join('performance_results', 'performance_results.xlsx'))
        ws = wb.active

        column_titles = {cell.value: cell.column for cell in ws[1]}

        for n in self.num_of_empty_cells_range:
            chart = LineChart()
            chart.title = f"Performance Comparison - {n} Empty Cells"
            chart.style = 13

            exact_column = column_titles[f'exact_{n}']
            exact_data = Reference(ws, min_col=exact_column, min_row=1, max_row=ws.max_row)
            chart.add_data(exact_data, titles_from_data=True)

            for p in self.genetic_algorithm_population_numbers:
                genetic_column = column_titles[f'genetic_{p}_{n}']
                genetic_data = Reference(ws, min_col=genetic_column, min_row=1, max_row=ws.max_row)
                chart.add_data(genetic_data, titles_from_data=True)

            chart.legend.position = 'r'
            chart.x_axis.title = "Trials"
            chart.y_axis.title = "Performance Score"

            ws.add_chart(chart, f"A{ws.max_row + 2}")

            wb.save(os.path.join('performance_results', 'performance_results.xlsx'))


if __name__ == '__main__':
    GENETIC_ALGORYTHM_POPULATION_NUMBERS = [5, 10, 20]
    NUM_OF_EMPTY_CELLS_RANGE = range(2, 7)
    runner = PerformanceRunner(NUM_OF_EMPTY_CELLS_RANGE, GENETIC_ALGORYTHM_POPULATION_NUMBERS)
    runner.main()
