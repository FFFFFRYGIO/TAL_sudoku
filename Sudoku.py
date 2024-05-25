from random import randint
from typing import List, Tuple


class Sudoku:
    """ Sudoku class with board of solution validation """

    def __init__(self, init_cells: List[Tuple[int, int, int]]):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.non_perm_cells_list = [(i, j) for i in range(9) for j in range(9)]

        for i, j, value in init_cells:
            if value not in range(1, 10):
                raise ValueError(f'Value {value} is not permitted for sudoku')
            self.board[i][j] = value
            self.non_perm_cells_list.remove((i, j))

        self.mark = None

    def mark_solution(self):
        """ update mark attribute according to current board """

        if not self.is_solved():
            raise ValueError('Sudoku is not solved yet')
        self.mark = self.count_mistakes()

    def is_solved(self) -> bool:
        """ check if whole board is filled with digits from 1 to 9 """

        return all(self.board[i][j] in range(1, 10) for i in range(9) for j in range(9))

    def is_valid(self) -> bool:
        """ check if board is solved without returning the amount of errors """

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
        """ count number of mistakes in board for rows, cols and 3x3 squares """

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
        """ print board in console """

        print("Sudoku:")
        for row in self.board:
            for value in row:
                print(value, end=" ")
            print()


def get_random_sudoku(num_of_empty_cells: int, good_solution) -> Sudoku:
    """ get a sudoku board with some randomly deleted cells """

    min_possible_clues = 17
    if not num_of_empty_cells or num_of_empty_cells > 9 * 9 - min_possible_clues:
        raise ValueError(f"Wrong number of empty cells: {num_of_empty_cells}")

    init_cells = good_solution.copy()
    for _ in range(num_of_empty_cells):
        init_cells.pop(randint(0, len(init_cells) - 1))

    return Sudoku(init_cells)
