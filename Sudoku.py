import random
from typing import List, Tuple


GOOD_SOLUTION = [
    (0, 0, 5), (0, 1, 3), (0, 2, 4), (0, 3, 6), (0, 4, 7), (0, 5, 8), (0, 6, 9), (0, 7, 1), (0, 8, 2),
    (1, 0, 6), (1, 1, 7), (1, 2, 2), (1, 3, 1), (1, 4, 9), (1, 5, 5), (1, 6, 3), (1, 7, 4), (1, 8, 8),
    (2, 0, 1), (2, 1, 9), (2, 2, 8), (2, 3, 3), (2, 4, 4), (2, 5, 2), (2, 6, 5), (2, 7, 6), (2, 8, 7),
    (3, 0, 8), (3, 1, 5), (3, 2, 9), (3, 3, 7), (3, 4, 6), (3, 5, 1), (3, 6, 4), (3, 7, 2), (3, 8, 3),
    (4, 0, 4), (4, 1, 2), (4, 2, 6), (4, 3, 8), (4, 4, 5), (4, 5, 3), (4, 6, 7), (4, 7, 9), (4, 8, 1),
    (5, 0, 7), (5, 1, 1), (5, 2, 3), (5, 3, 9), (5, 4, 2), (5, 5, 4), (5, 6, 8), (5, 7, 5), (5, 8, 6),
    (6, 0, 9), (6, 1, 6), (6, 2, 1), (6, 3, 5), (6, 4, 3), (6, 5, 7), (6, 6, 2), (6, 7, 8), (6, 8, 4),
    (7, 0, 2), (7, 1, 8), (7, 2, 7), (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 6, 6), (7, 7, 3), (7, 8, 5),
    (8, 0, 3), (8, 1, 4), (8, 2, 5), (8, 3, 2), (8, 4, 8), (8, 5, 6), (8, 6, 1), (8, 7, 7), (8, 8, 9),
]


class Sudoku:
    def __init__(self, init_cells: List[Tuple[int, int, int]]):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.non_perm_cells_list = [(i, j) for i in range(9) for j in range(9)]

        for i, j, value in init_cells:
            if value not in range(1, 10):
                raise ValueError(f'Value {value} is not permitted for sudoku')
            self.board[i][j] = value
            self.non_perm_cells_list.remove((i, j))

    def is_solved(self) -> bool:
        return all(self.board[i][j] in range(1, 10) for i in range(9) for j in range(9))

    def is_valid(self) -> bool:
        if not self.is_solved():
            raise ValueError('Sudoku is not solved yet')
        if self.__count_mistakes_in_rows(only_validation=True) == -1:
            return False
        if self.__count_mistakes_in_columns(only_validation=True) == -1:
            return False
        if self.__count_mistakes_in_squares(only_validation=True) == -1:
            return False
        return True

    def count_mistakes(self) -> int:
        if not self.is_solved():
            raise ValueError('Sudoku is not solved yet')
        count_mistakes_rows = self.__count_mistakes_in_rows()
        count_mistakes_cols = self.__count_mistakes_in_columns()
        count_mistakes_squares = self.__count_mistakes_in_squares()
        return count_mistakes_rows + count_mistakes_cols + count_mistakes_squares

    def __count_mistakes_in_rows(self, only_validation=False) -> int:
        mistake_count = 0
        for row in self.board:
            values_seen = set()
            for value in row:
                if value in values_seen:
                    if only_validation:
                        return -1
                    mistake_count += 1
                values_seen.add(value)
        return mistake_count

    def __count_mistakes_in_columns(self, only_validation=False) -> int:
        mistake_count = 0
        for col_index in range(9):
            values_seen = set()
            for row_index in range(9):
                value = self.board[row_index][col_index]
                if value in values_seen:
                    if only_validation:
                        return -1
                    mistake_count += 1
                values_seen.add(value)
        return mistake_count

    def __count_mistakes_in_squares(self, only_validation=False) -> int:
        mistake_count = 0
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                values_seen = set()
                for i in range(3):
                    for j in range(3):
                        value = self.board[start_row + i][start_col + j]
                        if value in values_seen:
                            if only_validation:
                                return -1
                            mistake_count += 1
                        values_seen.add(value)
        return mistake_count

    def display(self):
        print("Sudoku:")
        for row in self.board:
            for value in row:
                print(value, end=" ")
            print()


def get_random_sudoku(num_of_empty_cells: int, good_solution) -> Sudoku:
    min_possible_clues = 17
    if num_of_empty_cells > 9 * 9 - min_possible_clues:
        raise ValueError(f"Number of empty cells {num_of_empty_cells} requested exceeds the number of cells available")

    init_cells = good_solution.copy()
    for _ in range(num_of_empty_cells):
        init_cells.pop(random.randint(0, len(init_cells) - 1))

    return Sudoku(init_cells)
