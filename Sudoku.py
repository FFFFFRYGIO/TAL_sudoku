from typing import List, Tuple


INIT_CELLS = [
    (0, 0, 5), (0, 1, 3), (0, 4, 7),
    (1, 0, 6), (1, 3, 1), (1, 4, 9), (1, 5, 5),
    (2, 1, 9), (2, 2, 8), (2, 7, 6),
    (3, 0, 8), (3, 4, 6), (3, 8, 3),
    (4, 0, 4), (4, 3, 8), (4, 5, 3), (4, 8, 1),
    (5, 0, 7), (5, 4, 2), (5, 8, 6),
    (6, 1, 6), (6, 6, 2), (6, 7, 8),
    (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 8, 5),
    (8, 4, 8), (8, 7, 7), (8, 8, 9)
]
GOOD_SOLUTION = [
    (0, 2, 4), (0, 3, 6), (0, 5, 8), (0, 6, 9), (0, 7, 1), (0, 8, 2),
    (1, 1, 7), (1, 2, 2), (1, 6, 3), (1, 7, 4), (1, 8, 8),
    (2, 0, 1), (2, 3, 3), (2, 4, 4), (2, 5, 2), (2, 6, 5), (2, 8, 7),
    (3, 1, 5), (3, 2, 9), (3, 3, 7), (3, 5, 1), (3, 6, 4), (3, 7, 2),
    (4, 1, 2), (4, 2, 6), (4, 6, 7), (4, 7, 9),
    (5, 1, 1), (5, 2, 3), (5, 3, 9), (5, 5, 4), (5, 6, 8), (5, 7, 5),
    (6, 0, 9), (6, 2, 1), (6, 3, 5), (6, 4, 3), (6, 5, 7), (6, 8, 4),
    (7, 0, 2), (7, 1, 8), (7, 2, 7), (7, 6, 6), (7, 7, 3),
    (8, 0, 3), (8, 1, 4), (8, 2, 5), (8, 3, 2), (8, 5, 6), (8, 6, 1)
]


class Cell:
    def __init__(self, value: int, is_perm: bool = False):
        self.value = value
        self.is_perm = is_perm


class Sudoku:
    def __init__(self, init_cells: List[Tuple[int, int, int]]):
        self.board = [[Cell(0) for _ in range(9)] for _ in range(9)]
        for i, j, k in init_cells:
            self.board[i][j] = Cell(k, is_perm=True)

    def is_valid(self) -> bool:
        return self.count_mistakes() == 0

    def count_mistakes(self) -> int:
        count_mistakes_rows = self.__count_mistakes_in_rows()
        count_mistakes_cols = self.__count_mistakes_in_columns()
        count_mistakes_squares = self.__count_mistakes_in_squares()
        return count_mistakes_rows + count_mistakes_cols + count_mistakes_squares

    def __count_mistakes_in_rows(self) -> int:
        mistake_count = 0
        for row in self.board:
            values_seen = set()
            for cell in row:
                if cell.value in values_seen:
                    mistake_count += 1
                values_seen.add(cell.value)
        return mistake_count

    def __count_mistakes_in_columns(self) -> int:
        mistake_count = 0
        for col_index in range(9):
            values_seen = set()
            for row_index in range(9):
                value = self.board[row_index][col_index].value
                if value in values_seen:
                    mistake_count += 1
                values_seen.add(value)
        return mistake_count

    def __count_mistakes_in_squares(self) -> int:
        mistake_count = 0
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                values_seen = set()
                for i in range(3):
                    for j in range(3):
                        cell = self.board[start_row + i][start_col + j]
                        if cell.value in values_seen:
                            mistake_count += 1
                        values_seen.add(cell.value)
        return mistake_count
