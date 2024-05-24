import os
from random import choice
from typing import List, Tuple

from Sudoku import Sudoku

GOOD_SOLUTIONS = [
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ],
    [
        [8, 2, 7, 1, 5, 4, 3, 9, 6],
        [9, 6, 5, 3, 2, 7, 1, 4, 8],
        [3, 4, 1, 6, 8, 9, 7, 5, 2],
        [5, 9, 3, 4, 6, 8, 2, 7, 1],
        [4, 7, 2, 5, 1, 3, 6, 8, 9],
        [6, 1, 8, 9, 7, 2, 4, 3, 5],
        [7, 8, 6, 2, 3, 5, 9, 1, 4],
        [1, 5, 4, 7, 9, 6, 8, 2, 3],
        [2, 3, 9, 8, 4, 1, 5, 6, 7]
    ],
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
]


def save_good_solution(solution: List[List[int]], file_name: str = 'good_solution.txt'):
    with open(os.path.join('good_solutions', file_name), 'w') as f:
        for row in solution:
            f.write("\t".join(str(i) for i in row))
            f.write("\n")


def save_solutions(solutions: List[List[List[int]]], file_names: List[str] = None) -> List[str]:
    if not os.path.exists('good_solutions'):
        os.makedirs('good_solutions')

    if not file_names:
        file_names = [f'good_solution_{i}' for i in range(1, len(solutions) + 1)]
    for solution, file_name in zip(solutions, file_names):
        save_good_solution(solution, file_name)
    return file_names


def get_good_solution(file_name: str = None) -> List[Tuple[int, int, int]]:
    if file_name is None:
        file_name = choice(os.listdir('good_solutions'))

    good_solution = []
    with open(os.path.join('good_solutions', file_name), 'r') as f:
        i = j = 0
        for line in f:
            for value in line.strip().split():
                good_solution.append((i, j, int(value)))
                i, j = (i + 1, 0) if j == 8 else (i, j + 1)
    return good_solution


def get_solutions(solutions_file_list: List[str] = None) -> List[List[Tuple[int, int, int]]]:
    if not solutions_file_list:
        solutions_file_list = [f'good_solution_{i}' for i in range(1, len(GOOD_SOLUTIONS) + 1)]

    good_solutions = []
    for good_solution_file in solutions_file_list:
        good_solutions.append(get_good_solution(good_solution_file))
    return good_solutions


def get_problem(file_name: str) -> List[Tuple[int, int, int]]:
    file_path = os.path.join('problems_source', file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_name} does not exist in the problems_source directory.")

    good_solution = []
    with open(file_path, 'r') as f:
        i = j = 0
        for line in f:
            for value in line.strip().split('\t'):
                if value:
                    good_solution.append((i, j, int(value)))
                i, j = (i + 1, 0) if j == 8 else (i, j + 1)
    return good_solution


if __name__ == '__main__':
    def test_save_get_solutions():
        file_names = save_solutions(GOOD_SOLUTIONS)
        for solution in get_solutions(file_names):
            sudoku = Sudoku(solution)
            if not sudoku.is_valid():
                print('sudoku not valid')
                sudoku.display()


    test_save_get_solutions()
